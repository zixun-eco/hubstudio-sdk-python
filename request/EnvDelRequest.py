#!/usr/bin/python
# -*- coding: UTF-8 -*-
from request.BaseRequest import BaseRequest


class EnvDelRequest(BaseRequest):
    """删除环境"""

    def __init__(self):
        BaseRequest.__init__(self)

    def get_command(self):
        """请求命令"""
        return "/api/v1/env/del"
