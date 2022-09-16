#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from request.ClientCloseRequest import ClientCloseRequest


def close_client():
    request = ClientCloseRequest()
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print(response.message)


if __name__ == '__main__':
    close_client()
