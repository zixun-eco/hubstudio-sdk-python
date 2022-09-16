#!/usr/bin/python
# -*- coding: UTF-8 -*-
class BaseRequest:

    biz_model = {}
    """请求参数"""

    request_id = None
    """请求id"""

    def get_command(self):
        """请求命令"""
        raise Exception('未实现BaseRequest.get_command()方法')

