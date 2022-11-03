#!/usr/bin/python
# -*- coding: UTF-8 -*-
from request.BaseRequest import BaseRequest


class CookieExportRequest(BaseRequest):
    """导出指定环境的cookie"""

    def __init__(self):
        BaseRequest.__init__(self)

    def get_command(self):
        """请求命令"""
        return "/api/v1/env/export-cookie"
