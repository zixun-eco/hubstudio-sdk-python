#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.CookieExportModel import CookieExportModel
from request.CookieExportRequest import CookieExportRequest


def export_cookie(container_code):
    """导出环境的cookie"""
    request = CookieExportRequest()
    # 参数设置
    model = CookieExportModel()
    model.containerCode = container_code
    request.biz_model = model
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
        return response.result
    else:
        print("导出cookie失败")
        print(response.message)
        return ""


if __name__ == '__main__':
    export_cookie("50957154")
