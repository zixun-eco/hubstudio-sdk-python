#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import sys

from handler.ClientOpenHandler import open_client
from handler.EnvCreateHandler import create_env
from handler.EnvOpenHandler import open_env
from handler.WebdriverHandler import open_baidu, get_driver_by_version, get_driver_by_path

if __name__ == '__main__':

    # 启动客户端
    open_result = open_client(group_code="团队id")
    if not open_result:
        sys.exit()

    # 创建环境
    create_env_res = create_env()
    if not create_env_res.success:
        sys.exit()

    create_json = json.loads(create_env_res.result)
    container_code = create_json["containerCode"]
    core_version = create_json["coreVersion"]

    # 打开环境，获取调试端口
    env_open_result = open_env(container_code)
    if not env_open_result.success:
        sys.exit()
    env_reply_json = json.loads(env_open_result.result)

    # 获取webdriver
    # driver = get_driver_by_version(core_version, env_reply_json.get("debuggingPort"))
    driver = get_driver_by_path(env_reply_json.get("webdriver"), env_reply_json.get("debuggingPort"))
    # 运行脚本
    open_baidu(driver)
