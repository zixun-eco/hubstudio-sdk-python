#!/usr/bin/python
# -*- coding: UTF-8 -*-
import uuid

from config.CommandConfig import client
from model.ProxyUpdateModel import ProxyUpdateModel
from request.ProxyUpdateRequest import ProxyUpdateRequest


def update_proxy():
    """更新代理"""
    request = ProxyUpdateRequest()
    # 参数设置方法一
    model = ProxyUpdateModel()
    model.containerCode = 8252570
    model.asDynamicType = 2
    model.proxyTypeName = "不使用代理"
    # model.proxyHost = "127.0.0.1"
    # model.proxyPort = 8080
    # model.proxyAccount = "abc"
    # model.proxyPassword = "123"
    # model.referenceCity = "Shanghai"
    # model.referenceCountryCode = "China"
    request.biz_model = model
    # 参数设置方法二
    # request.biz_model = {
    #     "containerCode" = 8252570,
    #     "asDynamicType" = 2,
    #     "proxyTypeName" = "不使用代理"
    # }
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print("更新代理失败")
        print(response.message)


if __name__ == '__main__':
    update_proxy()
