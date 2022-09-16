#!/usr/bin/python
# -*- coding: UTF-8 -*-

class EnvListModel:
    """环境列表"""

    # 团队code 必填
    groupCode = None

    # 环境id列表
    containerCodes = []

    # 环境名称
    containerName = None

    # 创建开始时间
    createStartTime = None

    # 创建结束时间
    createEndTime = None

    # 环境类型 1自建环境 2环境转移
    createType = None

    # 代理ip查询
    ipAddress = None

    # 代理ip类型列表
    proxyTypeNames = []

    # 不为空既是查询未分组
    noTag = None

    # 备注
    remark = None

    # 环境分组名称数组
    tagNames = []

    # 分页第几页偏移量
    current = None

    # 分页条数
    size = None
