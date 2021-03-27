#coding=utf-8

import os
import unittest 
from utils.case_util import CaseUtil

'''
@ 作者：吴剑辉（福建中测）
@ 时间：2021-03-17
@ 说明：程序入口
@ 参数：
'''
if __name__ == "__main__":
    # 获取测试用例套件
    case_util = CaseUtil()    
    suite = case_util.get_case_suite()
    # 执行用例套件
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
    '''
    # 自动构造测试集，执行指定目录下所有用例文件及用例，但是用例执行顺序以文件名和用例名的ASCII码从小到大排序
    test_dir = os.path.join(os.getcwd(), "cases/businesses")
    discover = unittest.defaultTestLoader.discover(test_dir, "*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(discover)
    '''

    '''
    # 手动构造测试集合，可以指定待执行用例及用例执行顺序
    suite = unittest.TestSuite()
    # 添加用例对应的类和方法
    suite.addTest(BusinessCase("test_business"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''