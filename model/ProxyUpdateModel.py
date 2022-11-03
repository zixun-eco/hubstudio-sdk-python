#!/usr/bin/python
# -*- coding: UTF-8 -*-

class ProxyUpdateModel:
    """更新代理"""

    # 环境id 必填
    containerCode = None

    # 使用方式 1静态 2动态 必填
    asDynamicType = None

    # 代理帐号
    proxyAccount = None

    # 代理主机地址
    proxyHost = None

    # 代理密码
    proxyPassword = None

    # 代理端口
    proxyPort = None

    # 代理类型
    proxyTypeName = None

    # 参考城市
    referenceCity = None

    # 参考国家代码
    referenceCountryCode = None

    # 参考州
    referenceRegionCode = None
