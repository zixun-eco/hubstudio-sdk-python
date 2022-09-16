#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.EnvCreateModel import EnvCreateModel
from request.EnvCreateRequest import EnvCreateRequest


def create_env():
    """创建环境"""
    request = EnvCreateRequest()
    # 参数设置方法一
    model = EnvCreateModel()
    model.groupCode = 10814480
    model.asDynamicType = 2
    model.containerName = "新环境6"
    model.proxyTypeName = "HTTP"
    request.biz_model = model
    # 参数设置方法二
    # request.biz_model = {
    #     "groupCode": 10814480,
    #     "asDynamicType" = 2,
    #     "containerName" = "新环境6",
    #     "proxyTypeName" = "HTTP"
    # }
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print("创建环境失败")
        print(response.message)


if __name__ == '__main__':
    create_env()
