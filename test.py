#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import sys

from handler.ClientOpenHandler import open_client
from handler.EnvListHandler import list_env
from handler.EnvOpenHandler import open_env
from handler.WebdriverHandler import open_baidu, get_driver

if __name__ == '__main__':

    # 启动客户端
    open_result = open_client(group_code="10814480")
    if not open_result.success:
        sys.exit()

    # 获取环境列表
    # list_env_result = list_env()
    # if not list_env_result.success:
    #     sys.exit()

    # 打开环境，获取webdriver调试端口
    env_open_result = open_env("10814480", "8252770")
    if not env_open_result.success:
        sys.exit()
    env_reply_json = json.loads(env_open_result.result)
    print("env_open_result:", env_open_result)

    # 获取webdriver
    driver = get_driver(env_reply_json.get("debuggingPort"))
    # 运行脚本
    open_baidu(driver)
