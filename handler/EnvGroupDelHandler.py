#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.EnvGroupDelModel import EnvGroupDelModel
from request.EnvGroupDelRequest import EnvGroupDelRequest


def delete_env_group(tag_code):
    """删除分组"""
    request = EnvGroupDelRequest()
    # 参数设置
    model = EnvGroupDelModel()
    model.tagCode = tag_code
    request.biz_model = model
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
        return response.result
    else:
        print("删除分组失败:", response.requestId)
        print(response.message)
        return None


if __name__ == '__main__':
    delete_env_group(8281070)  # 分组id
