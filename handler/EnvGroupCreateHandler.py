#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.EnvGroupCreateModel import EnvGroupCreateModel
from request.EnvGroupCreateRequest import EnvGroupCreateRequest


def create_env_group():
    """创建环境分组"""
    request = EnvGroupCreateRequest()
    # 参数设置方法一
    model = EnvGroupCreateModel()
    model.groupCode = 10814480
    model.tagName = "测试分组2"
    request.biz_model = model
    # 参数设置方法二
    # request.biz_model = {
    #     "groupCode": 10814480,
    #     "asDynamicType" = 2,
    #     "tagName" = "测试分组"
    # }
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print("创建环境分组失败")
        print(response.message)


if __name__ == '__main__':
    create_env_group()
