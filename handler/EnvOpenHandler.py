#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.EnvOpenModel import EnvOpenModel
from request.EnvOpenRequest import EnvOpenRequest


def open_env(group_code, container_code):
    """打开环境"""
    request = EnvOpenRequest()
    # 参数设置方法一
    model = EnvOpenModel()
    model.groupCode = group_code
    model.containerCode = container_code
    model.isHeadless = False
    model.isWebDriverReadOnlyMode = True
    request.biz_model = model
    # 参数设置方法二
    # request.biz_model = {
    #     "groupCode": "",
    #     "containerCode": "",
    #     "isHeadless": False,
    #     "isWebDriverReadOnlyMode": True
    # }
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print("打开环境失败")
        print(response.message)
    return response


if __name__ == '__main__':
    open_env("10814480", "8252770")
