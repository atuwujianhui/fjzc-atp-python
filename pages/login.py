#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者：吴剑辉（福建中测）
# 时间：2021-03-20
# 文件：login.py
# 说明：

import os
import sys
sys.path.append(os.getcwd())
from utils.web_element_util import WebElementUtil

'''
@ 作者：吴剑辉（福建中测）
@ 时间：2021-03-20
@ 说明：登录
@ 参数：
'''
class Login():

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-20
    @ 说明：
    @ 参数：
    '''
    def __init__(self, web_element_util: WebElementUtil):
        self.web_element_util = web_element_util
        self.driver = web_element_util.get_driver()

    def login(self, name, password):
        self.driver.get("https://www.imooc.com/")
        # 点击登录
        self.web_element_util.click("LOGIN.login_link")
        # 输入登录邮箱
        self.web_element_util.send_keys("LOGIN.email", name)
        # 输入密码
        self.web_element_util.send_keys("LOGIN.password", password)
        # 点击登录
        self.web_element_util.click("LOGIN.login_button")

'''
@ 作者：吴剑辉（福建中测）
@ 时间：2021-03-20
@ 说明：
@ 参数：
'''
if __name__ == "__main__":
    pass