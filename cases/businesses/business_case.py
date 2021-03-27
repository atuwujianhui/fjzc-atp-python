#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者：吴剑辉（福建中测）
# 时间：2021-03-20
# 文件：business_case.py
# 说明：

import time
import unittest
import os
import sys
sys.path.append (os.getcwd())
from pages.login import Login
from cases.base_case import BaseCase
from ddt import ddt, data, unpack
# 客户端（Python代码+ selenium库） -> web driven -> 浏览器

'''
@ 作者：吴剑辉（福建中测）
@ 时间：2021-03-17
@ 说明：场景自动化测试主程序
@ 参数：
'''
@ddt
class BusinessCase(BaseCase):

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-17
    @ 说明：每个case执行的前置操作(保留)
    @ 参数：
    '''
    def setUp(sel):
        #print单介case执行之前的前置条件。m
        pass

    # ************************************
    # ********** 用侧设计 - 开始 **********
    # ************************************

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-17
    @ 说明：实际业务场景示例，待完善。
    @ 参数：
    '''
    @data(("179988030@qq.com", "wujianhui2"))
    @unpack
    def test_business_case(self, username = None, password = None):
        #登录网贷平台
        Login(self.web_element_util).login(username, password)
        #其他业务步骤，待补充+
        return False

    # ************************************
    # ********** 用侧设计 - 结束 **********
    # ************************************

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-17
    @ 说明：每个case执行的前置操作（保留）
    @ 参数：
    '''
    def tearDown(self):
        #print("单个case执行之后的后置条件。.
        pass

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-17
    @ 说明：测试
    @ 参数：
    '''
if __name__ == "__main__":
    # 全部执行test”开头的case，是“urittest~的功能特性，但是按照方法名称的ASC码
    unittest.main()
    # 手动构造测试集合，可以指定待执行用例及用例执行顺序
    # suite = unittest.TestSuite()
    # 添加用例对应的类和方法
    # suite.addTest(BusinessCase("business_case_01"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # print(unittest.TestLoader().getTestCaseNames(BusinessCase))