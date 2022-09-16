#!/usr/bin/python
# -*- coding: UTF-8 -*-
import subprocess
import uuid

from config.CommandConfig import client, CommandConfig
from model.ClientOpenModel import ClientOpenModel
from request.ClientOpenRequest import ClientOpenRequest


def open_client(group_code):
    """打开客户端-首次启动"""
    path = CommandConfig.connector_path
    socket_port = CommandConfig.socket_port
    cmd = [path, '--socket_port='+str(socket_port), '--client_path='+CommandConfig.hubstudio_path]
    try:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        line = p.stdout.readline()
        line_str = line.decode(encoding="utf-8").strip()
        while line is not None and line_str != "":
            line_str = line.decode(encoding="utf-8").strip()
            if "Startup complete" == line_str:  # 判断程序正确执行完毕后退出到后台执行
                break
            if "Update complete, need reopen" == line_str:  # 判断更新完成需要重新启动
                print("程序更新完成，请重新启动")
                return
            if "Program started" in line_str:  # 判断程序已启动
                print("程序已启动，无需重复启动")
                return
            line = p.stdout.readline()
    except Exception as err:
        print(err)

    return open_client_change_team(group_code)


def open_client_change_team(group_code):
    """打开客户端-更换团队"""
    print("打开客户端，获取坐席...")
    request = ClientOpenRequest()
    model = ClientOpenModel()
    model.groupCode = group_code
    request.biz_model = model
    request.request_id = str(uuid.uuid4())

    # 创建请求
    response = client.execute(request)
    if response.success:
        print(response.result)
    else:
        print(response.message)
    return response


if __name__ == '__main__':
    open_client("10814480")
