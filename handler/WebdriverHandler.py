#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

from selenium import webdriver
from config.CommandConfig import CommandConfig


# 获取webdriver
def get_driver(port):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_experimental_option("debuggerAddress", '127.0.0.1:' + str(port))
    return webdriver.Chrome(CommandConfig.webdriver_path, options=options)


def open_baidu(driver):
    driver.get("https://www.baidu.com/")
    driver.implicitly_wait(10)
    driver.find_element_by_class_name('s_ipt').send_keys('hubstudio')
    time.sleep(1)
    driver.find_element_by_id("su").click()
    time.sleep(6)
