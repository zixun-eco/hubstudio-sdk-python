#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from request.EnvGroupListRequest import EnvGroupListRequest


def list_env_group():
    """获取分组列表"""
    request = EnvGroupListRequest()
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
        return response.result
    else:
        print("获取分组列表失败:", response.requestId)
        print(response.message)
        return None


if __name__ == '__main__':
    list_env_group()
