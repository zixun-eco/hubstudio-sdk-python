#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import UserDict


class BaseResponse(UserDict):

    __setitem__ = UserDict.__setattr__
    __getitem__ = UserDict.__getattribute__

    """返回类"""
    requestId = None
    success = None
    result = None
    message = None

    def __init__(self, _dict=None, **kwargs):
        UserDict.__init__(self, _dict, **kwargs)
