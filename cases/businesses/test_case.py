#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者：吴剑辉（福建中测）
# 时间：2021-03-20
# 文件：test_case.py
# 说明：

from selenium import webdriver
import time
import unittest
import os
import sys
sys.path.append(os.getcwd())
from pages.login import Login
from cases import base_case
from ddt import ddt, data, unpack
#客户端(Python代码+selenium库) >web driver-、浏览器-

data_list = [{"id": "1", "name": "Hello"}, {"id": "2", "name": "Hadoop"}]

'''
@ 作者：吴剑辉（福建中测）
0 时间：2021-03-17
@ 说明：场景自动化测试主程序
@ 参数：
'''

@ddt
class TestCase(base_case.BaseCase):

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-18
    @ 说明：覆写父类方法，不启动浏览器
    @ 参数：
    '''
    @classmethod
    def setUpClass(self):
        pass

    '''
    @ 作者：吴剑辉
    @ 时间：2021-03-17
    @ 说明：每个case执行的前置操作(保留）
    @ 参数：
    '''
    def setUp(self):
        # print(“单个case执行之前的前置条件。")
        pass

    # ************************************
    # ********** 用侧设计 - 开始 **********
    # ************************************

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-18
    @ 说明：unittest断言示例。
    @ 参数：
    '''
    def hello_1(self):
        print("Hello World -1!")
        self.assertEqual(1, 2, "用例执行错误!")

    '''
    @ 作者：吴剑辉
    @ 时间：2021-03-18
    @ 说明：unittest普通测试用例
    @ 参数：
    '''
    # @data (("Hello", 1"), ("Hadoop", "2"), ("Kitty", "3"), ("Hive", "4"))
    @data(*data_list)
    def test_hello_2(self, info):
        print("Hello", info)

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-18
    @ 说明：unittest普通测试用例
    @ 叁数：
    '''
    def hello_3(self):
        print("Hello World - 3!")
    
    # ************************************
    # ********** 用侧设计 - 结束 **********
    # ************************************

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-19
    @ 说明：每个case执行的前置操作(保留)
    @ 参数：
    '''
    def tearDown(self):
        # print("单个case执行之后的后置条件。")
        pass

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-19
    @ 说明：覆写父类方法，不启动浏览器
    @ 参数：
    '''
    @classmethod
    def tearDownClass(self):
        pass

'''
@ 作者：吴剑辉（福建中测）
@ 时间：2021-03-16
@ 说明：测试
'''
if __name__ == "__main__":
    print(unittest.TestLoader().getTestCaseNames(TestCase))
    unittest.main()