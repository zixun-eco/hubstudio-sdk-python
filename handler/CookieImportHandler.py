#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.CookieImportModel import CookieImportModel
from request.CookieImportRequest import CookieImportRequest


def import_cookie(container_code, cookie):
    """向环境导入cookie"""
    request = CookieImportRequest()
    # 参数设置
    model = CookieImportModel()
    model.containerCode = container_code
    model.cookie = cookie
    request.biz_model = model
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print("导入cookie失败")
        print(response.message)


if __name__ == '__main__':
    import_cookie("50957154", "[{\"Name\":\"CONSENT\",\"Value\":\"PENDING+571\",\"Domain\":\".google.com\",\"Path\":\"/\",\"Secure\":true,\"HttpOnly\":false,\"Persistent\":\"1\",\"Creation\":\"2022-09-14T15:18:07.389+08:00\",\"LastAccess\":\"2024-09-13T15:18:07.389+08:00\",\"Expires\":\"2024-09-13T15:18:07.389+08:00\",\"Priority\":\"1\",\"HasExpires\":\"1\",\"Samesite\":\"-1\",\"SourceScheme\":\"2\",\"Firstpartyonly\":\"\",\"schemeMap\":false,\"isSelf\":false}]")
