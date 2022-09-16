#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.EnvUpdateModel import EnvUpdateModel
from request.EnvUpdateRequest import EnvUpdateRequest


def update_env():
    """更新环境"""
    request = EnvUpdateRequest()
    # 参数设置方法一
    model = EnvUpdateModel()
    model.groupCode = 10814480
    model.containerCode = 8252570
    model.containerName = "新环境4-更新"
    model.remark = "测试"
    model.tagName = "测试分组"
    request.biz_model = model
    # 参数设置方法二
    # request.biz_model = {
    #     "groupCode": 10814480,
    #     "containerCode" = 8252570,
    #     "containerName" = "新环境4-更新",
    #     "remark" = "测试"
    # }
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print("更新环境失败")
        print(response.message)


if __name__ == '__main__':
    update_env()
