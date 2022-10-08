#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import sys

from handler.ClientOpenHandler import open_client
from handler.EnvOpenHandler import open_env
from handler.PlaywrightHandler import get_browser_context, open_baidu

if __name__ == '__main__':
    '''需要安装playwright依赖: pip install playwright '''

    # 启动客户端
    open_result = open_client(group_code="10814480")
    if not open_result.success:
        sys.exit()

    # 打开环境，获取webdriver调试端口
    env_open_result = open_env(group_code="10814480", container_code="36767766")
    if not env_open_result.success:
        sys.exit()
    env_reply_json = json.loads(env_open_result.result)
    print("env_open_result:", env_open_result)

    # 获取playwright浏览器会话
    browser_context = get_browser_context(env_reply_json.get("debuggingPort"))
    # 运行脚本
    open_baidu(browser_context)



