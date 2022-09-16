#!/usr/bin/python
# -*- coding: UTF-8 -*-
from request.BaseRequest import BaseRequest


class EnvCreateRequest(BaseRequest):
    """创建环境"""

    def __init__(self):
        BaseRequest.__init__(self)

    def get_command(self):
        """请求命令"""
        return "env-create"
