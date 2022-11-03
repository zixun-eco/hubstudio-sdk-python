#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.EnvGroupCreateModel import EnvGroupCreateModel
from request.EnvGroupCreateRequest import EnvGroupCreateRequest


def create_env_group(tag_name: str):
    """创建环境分组"""
    request = EnvGroupCreateRequest()
    # 参数设置
    model = EnvGroupCreateModel()
    model.tagName = tag_name
    request.biz_model = model
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
        return response.result
    else:
        print("创建环境分组失败")
        print(response.message)
        return None


if __name__ == '__main__':
    create_env_group("测试分组")
