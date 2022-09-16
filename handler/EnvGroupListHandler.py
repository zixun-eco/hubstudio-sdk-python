#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.EnvGroupListModel import EnvGroupListModel
from request.EnvGroupListRequest import EnvGroupListRequest


def list_env_group():
    """获取分组列表"""
    request = EnvGroupListRequest()
    # 参数设置方法一
    model = EnvGroupListModel()
    model.groupCode = 10814480
    request.biz_model = model
    # 参数设置方法二
    # request.biz_model = {
    #     "groupCode": 10814480
    # }
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print("获取分组列表失败:", response.requestId)
        print(response.message)


if __name__ == '__main__':
    list_env_group()
