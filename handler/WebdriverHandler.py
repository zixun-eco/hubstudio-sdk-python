#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

from selenium import webdriver
from config.CommandConfig import CommandConfig


# 获取webdriver(100内核)
def get_driver(port):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", '127.0.0.1:' + str(port))
    return webdriver.Chrome(CommandConfig.webdriver_path_100, options=options)


# 根据内核版本获取webdriver
def get_driver_by_version(core_version, port):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", '127.0.0.1:' + str(port))
    if core_version == 100:
        return webdriver.Chrome(CommandConfig.webdriver_path_100, options=options)
    elif core_version == 105:
        return webdriver.Chrome(CommandConfig.webdriver_path_105, options=options)
    else:
        print("未找到对应版本webdriver。版本:", core_version)
        return None


def open_baidu(driver):
    driver.get("https://www.baidu.com/")
    driver.implicitly_wait(10)
    driver.find_element_by_class_name('s_ipt').send_keys('hubstudio')
    time.sleep(1)
    driver.find_element_by_id("su").click()
    time.sleep(6)
