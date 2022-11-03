#!/usr/bin/python
# -*- coding: UTF-8 -*-

class EnvOpenModel:

    def __init__(self):
        # 环境code
        self.containerCode = None
        # 是否无头模式
        self.isHeadless = False
        self.isWebDriverReadOnlyMode = True
        # 启动参数
        self.args = []

    def add_argument(self, argument):
        if argument:
            self.args.append(argument)
