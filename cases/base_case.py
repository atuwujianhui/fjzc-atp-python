#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者：吴剑辉（福建中测）
# 时间：2021-03-20
# 文件：base_case.py
# 说明：

import unittest
import os
import sys
import time
sys.path.append(os.getcwd())

from selenium import webdriver
from utils.web_element_util import WebElementUtil

#客户端( Python代码+ selenium库)web driver ->浏览器
'''
@ 作者：吴剑辉.
@ 时间：2021-03-17
@ 说明：自动化测试框架用例基类。
@ 参数：
'''
class BaseCase(unittest.TestCase):
    
    '''
    @ 作者：吴剑辉
    @ 时间：2021-03-17
    @ 说明：所有case执行的前置操作，可以替换“__init__”方法
    @ 参数：
    '''
    @classmethod
    def setUpClass(self):
        #新版本的Chrome驱动器需要禁用GPU加速：
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--disable-gpu")
        chrome_option.add_argument('–log-level=3')
        chrome_option.add_experimental_option('excludeSwitches', ['enable-logging'])
        #打开Chrome浏览器
        self.driver = webdriver.Chrome(options = chrome_option)
        #窗口最大化
        self.driver.maximize_window()
        #创建网页元素工具对象
        self.web_element_util = WebElementUtil(self.driver)
    
    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-17
    @ 说明：每一用例执行的前置操作（保留）
    @ 参数
    '''
    def setup(slef):
        # print("单个case执行之前的前置条件。")
        pass

    # ************************************
    # ********** 用侧设计 - 开始 **********
    # ************************************
    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-17
    @ 说明：业务场景示例，待完善。
    @ 参数：
    '''
    def business(self):
        pass

    # ************************************
    # ********** 用侧设计 - 结束 **********
    # ************************************

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-17
    @ 说明：每个用例执行的前置操作(保留) 
    @ 参数：
    '''
    def tearDown(self):
        # print("单个case执行之后的后置条件。")
        pass

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-17
    @ 说明：所有用例执行的后置操作，退出浏览器
    @ 参数：
    '''
    @classmethod
    def tearDownClass(self):
        #等待3秒
        time.sleep(5)
        #关闭浏览器
        self.driver.quit()

'''
@ 作者：吴剑辉（福建中测）
@ 时间：2021-03-17
@ 说明：测试
@ 参数：
'''
if __name__ == "__main__":
    #全部执行“test”开头的case，是“unittest”的功能特性，但是按照方法名称的ASCII码
    # unittest.main()
    suite = unittest.TestSuite()