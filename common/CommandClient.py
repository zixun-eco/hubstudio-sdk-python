#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import socket
import traceback

from request import BaseRequest
from response.BaseResponse import BaseResponse


def receive_data(socket_client):
    result = b''
    while True:
        reply = socket_client.recv(1024)
        result += reply
        if reply == b'' or result.endswith(b"\r\n"):
            break
    socket_client.shutdown(2)
    return result.decode('utf-8')


def send_socket(params: str, socket_port):
    try:
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_client.settimeout(300)  # 超时时间
        ip = '127.0.0.1'
        socket_client.connect((ip, socket_port))
        # print('Socket Connected to ' + ip)
        message = (params.encode('utf-8') + b"\r\n")
        socket_client.sendall(message)
        print('Message send successfully: %s' % params)
    except Exception as e:
        print('Failed to create socket or send message: %s' % params)
        print(traceback.print_exc())
        # print(e)
        return BaseResponse({"success": False, "message": "socket连接失败"})
        # sys.exit()
    # 接收数据
    result = receive_data(socket_client)

    response_dict = json.loads(result)
    return BaseResponse(response_dict)


class CommandClient:
    __app_id = ''
    __private_key = ''
    __socket_port = 6873

    def __init__(self, app_id, private_key, socket_port: int = 6873):
        """客户端

        :param app_id: 用户凭证ID
        :type app_id: str

        :param private_key: 用户凭证私钥
        :type private_key: str

        :param socket_port: 启动连接端口
        :type socket_port: int

        """
        self.__app_id = app_id
        self.__private_key = private_key
        self.__socket_port = socket_port

    def execute(self, request):
        param_str = self._build_params(request)
        return send_socket(param_str, self.__socket_port)

    def _build_params(self, request: BaseRequest):
        all_params = {
            'command': request.get_command(),
            'appId': self.__app_id,
            'privateKey': self.__private_key,
            'requestId': request.request_id,
        }
        # 添加业务参数
        biz_model = request.biz_model
        if biz_model is None:
            biz_model = {}
        if isinstance(biz_model, dict):
            all_params['bizContent'] = biz_model
        else:
            all_params['bizContent'] = biz_model.__dict__
        return json.dumps(all_params)


