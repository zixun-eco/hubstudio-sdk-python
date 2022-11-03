#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.RandomUaModel import RandomUaModel
from request.RandomUaRequest import RandomUaRequest


def random_ua(system_type=None, phone_model=None, version=None):
    """获取随机UA"""
    request = RandomUaRequest()
    # 参数设置
    model = RandomUaModel()
    model.type = system_type
    model.phoneModel = phone_model
    model.version = version
    request.biz_model = model
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
        return response.result
    else:
        print("获取随机UA失败")
        print(response.message)
        return None


if __name__ == '__main__':
    random_ua("windows")
    random_ua("windows", version=[100, 101])
    random_ua("android", "三星Galaxy S9+", [105, 98])
