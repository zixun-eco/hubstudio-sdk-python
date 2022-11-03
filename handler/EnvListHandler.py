#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.EnvListModel import EnvListModel
from request.EnvListRequest import EnvListRequest


def list_env():
    """获取环境列表"""
    request = EnvListRequest()
    # 参数设置方法一
    model = EnvListModel()
    model.current = 1
    model.size = 10
    # model.noTag = 1
    # model.containerCodes = [8254560]
    request.biz_model = model
    # 参数设置方法二
    # request.biz_model = {
    #     "current" = 1,
    #     "size" = 10
    # }
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print("获取环境列表失败:", response.requestId)
        print(response.message)
    return response


if __name__ == '__main__':
    list_env()
