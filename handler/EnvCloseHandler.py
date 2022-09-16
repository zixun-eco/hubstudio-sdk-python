#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.EnvCloseModel import EnvCloseModel
from request.EnvCloseRequest import EnvCloseRequest


def close_env(group_code, container_code):
    """关闭环境"""
    request = EnvCloseRequest()
    # 参数设置方法一
    model = EnvCloseModel()
    model.groupCode = group_code
    model.containerCode = container_code
    request.biz_model = model
    # request.biz_model = {
    #     "groupCode": group_code,
    #     "containerCode": container_code
    # }
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print("关闭环境失败")
        print(response.message)


if __name__ == '__main__':
    close_env("11236255", "36598110")
