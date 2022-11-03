#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.EnvOpenModel import EnvOpenModel
from request.EnvOpenRequest import EnvOpenRequest


def open_env(container_code):
    """打开环境"""
    request = EnvOpenRequest()
    # 参数设置方法一
    model = EnvOpenModel()
    model.containerCode = container_code
    model.isHeadless = False
    model.isWebDriverReadOnlyMode = True
    model.add_argument("--disable-extensions")  # 禁用插件
    model.add_argument("--blink-settings=imagesEnabled=false")  # 禁止加载图片
    request.biz_model = model
    # 参数设置方法二
    # request.biz_model = {
    #     "containerCode": "",
    #     "isHeadless": False,
    #     "isWebDriverReadOnlyMode": True,
    #     "args": ["--disable-extensions", "--blink-settings=imagesEnabled=false"]
    # }
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print("打开环境失败")
        print(response.message)
    return response


if __name__ == '__main__':
    open_env("8252770")
