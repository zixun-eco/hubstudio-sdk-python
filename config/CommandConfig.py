#!/usr/bin/python
# -*- coding: UTF-8 -*-
from common.CommandClient import CommandClient


class CommandConfig:
    # 应用id
    app_id = '202208111007337465826111488'
    # 应用私钥
    private_key = "MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCTm6UOHKwLbVU8uKT2xxZcGVxPC/lJYeOWGeJuUvk9n3mXPX/BLaKQz9V0VIBoUEnG5+rYSN6UCVOYnbpFrXKeoZOT0yCV7q4amsZKbo84PpxDA+Mas+61B1X72rXZEMyaX73JiEZOlbq/3e/mqJaiZMMTZvgkmZAep8kNgnPr3yhRTaUITIran5f+DjFvl5g5wlDQAIVwqhC9MrDlSklqmPfjwJ4gLA2ciyJLgTJ+1X922vKHKZU4HvXRnnTCPBOMERXteWsFVnEl8lhGcvaIXFqTQxGktdzt/aezIhffiKxl94QE9i8jb1uMFdMtyqWBZji8LD2MhgGcR6784JCRAgMBAAECggEAc+ldi99oGvEYZj55DHD6Vgh0PH6im8WK+mwJK6lsn7+DtAhPMlurtRv/+wIAc+nYhaHJAV73qjhItSfnBqBVycwIH6VDiXmMrservvdi8D/6ZYW/6VAyu2WvV78/3d0bTn6wgnnI/B0IMXMO2Iq6/3sw1SOe6N7OFcScVUeD0EyTft1A17RaBCm21v/sQNP9f6Gr1cuYK1SzuphtnSK3WYrs7CHpxGVH7YdHPkAjFywXRMX+3FiBaPTag2C/bd3TpjJtJPNwYy/CUeeXANN0HNMwocQYDCRsv39Vv/y8KDFX2zzg4DTXtk1fYpXkbO5lOxgXElq12qTsZTFS/pEfgQKBgQDOOc4llZTv33oDHdzoJvjnEe3TVEzl7LLPDG8w77ouoMf+eGmkAOUeHtoNwwwN+q6DYKna/RYk1xtb+MUMzylH6a45chKoalddIri/c0Td6BlFO8Q+TJRobJH0GG070ub1mlGud6Ji1Wp6m+33zl/JfhvbY5j6YS9juAbBp5cZbQKBgQC3O/x0etlsI9adHBcBaRdbsrfSFvGsX+M0ZwsCk/HRgUJRSnmb5X/woY0Am6569Dfx70k6tNGW+P/DbnYk0pMgTDNAAw8a/x6RejOz7FFy/6dW0cLnzDCczFWCgDsG7HM7xFd/XvpMyVuQMdSmoWxIAjCG616SsUYbUHeQfg5hNQKBgFpZ9xh+XZ9ukL1W0xcfJAPQ1hq1n29I8dpGv1x4W2DcbmLuDJKfFcLJj41h/CEPyG+k5SYdphsD52e3KVYAWTy5g+yFLul8lcQnVzwB25VBf/jWQ5dr48WQc623GfyQ3UGTl9/RaGLWz+zh7jOYxly4FKpdC4P/Gk0dLlCgBVJNAoGBAKgcgSLdE14EA4NhojnJEYUwEzbNli1wTCRn5dIXqmVtEktC6Q//H8LGdXd5XjuwlSODRsx12VWKXh4P2pUuHY4kW2D/bXx3VLRkSctppdC8fetJyGijDnbNgiaZP466oX7URPK3US3iD//buB6pO49VcvBWQg6UVp341bnb7ZWBAoGBAKING+yxGfR+XHdPc5Ykd2hQoA1fNNTIkbZ9sLj8SGVUbpuBuM+PRp8NBK/YyRbxxvBvjc5c6ns6zeiWzQidYQNNXBbvYgy9dwLJogyS+NUsY0UAqFhuQ0IO9Yo8VYYiRLItoh15qk2ElPGvkOegGVEsbpMV2vhYzImpGFXIBCi3"
    # 执行文件路径
    connector_path = r"D:\Hubstudio\2.12.0.1\hubstudio_connector.exe"
    # hubstudio程序路径
    hubstudio_path = r"D:\Hubstudio\2.12.0.1\Hubstudio.exe"
    # 连接端口
    socket_port = 6873
    # webdriver程序路径
    webdriver_path_100 = r".\config\chromedriver100.exe"
    webdriver_path_105 = r".\config\chromedriver105.exe"


def create_client():
    """
    可以以导入模块的方式获得一个单例对象
    Example:
    from config.CommandConfig import client
    response = client.execute(request)
    """
    # 应用id
    app_id = CommandConfig.app_id
    # 应用私钥
    private_key = CommandConfig.private_key
    # 连接端口
    socket_port = CommandConfig.socket_port
    # 创建请求客户端
    return CommandClient(app_id, private_key, socket_port)


client = create_client()
