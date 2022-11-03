#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.EnvDelModel import EnvDelModel
from request.EnvDelRequest import EnvDelRequest


def del_env(container_code: str):
    """删除环境"""
    return del_env_list([container_code])


def del_env_list(container_codes: list):
    """批量删除环境"""
    request = EnvDelRequest()
    # 参数设置
    model = EnvDelModel()
    model.containerCodes = container_codes
    request.biz_model = model
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print("删除环境失败")
        print(response.message)
    return response


if __name__ == '__main__':
    del_env("8299847")
