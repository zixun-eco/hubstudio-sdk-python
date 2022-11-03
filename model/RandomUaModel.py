#!/usr/bin/python
# -*- coding: UTF-8 -*-

class RandomUaModel:
    """获取随机UA"""

    # 操作系统参数：windows、android、ios（不传参数默认windows）
    type = None

    # type选择android和ios时，机型必填。机型参数包括：“google Pixel 4、红米8、红米7、google Pixel 5a、三星Galaxy Note8、
    # 小米10、三星Galaxy S9+、小米9、iPhone 6 Plus、iPhone 8 Plus、iPhone SE 2、iPhone 7 Plus、iPhone X、iPhone13 Pro、
    # iPhone XS、iPhone 13 Pro Max、iPhone 12 mini、iPhone 8、iPhone 13 mini、iPhone 6、iPhone 12 Pro Max、iPhone 7、
    # iPhone 12 、iPhone 12 Pro、iPhone 11 Pro、iPhone 13”
    phoneModel = None

    # 支持数组，不传参默认随机。范围包括95、96、97、98、99、100、101、102、103、104、105、106
    version = []
