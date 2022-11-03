#!/usr/bin/python
# -*- coding: UTF-8 -*-
from playwright import sync_api


# 获取playwright浏览器会话
def get_browser_context(port):
    playwright = sync_api.sync_playwright().start()
    browser = playwright.chromium.connect_over_cdp("http://127.0.0.1:" + str(port))
    context = browser.contexts[0]
    return context


def open_baidu(browser_context):
    # 使用第一个标签页打开playwright官网
    page = browser_context.pages[0]
    page.goto("https://playwright.dev/")
    print(page.title())

    # 新建标签页
    new_page = browser_context.new_page()
    # 打开百度
    new_page.goto("https://www.baidu.com")
    print(new_page.title())
    # 输入hubstudio并搜索
    new_page.fill('input[name="wd"]', 'hubstudio')
    new_page.press('input[id="su"]', 'Enter')
