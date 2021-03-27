#coding=utf-8

import os
import sys
import unittest
sys.path.append(os.getcwd())
from utils.yaml_file_util import case_suite_configs

# 模块根目录：cases.businesses
module_root_dir = "cases.businesses"
class CaseUtil:

    '''
    @作者：吴剑辉
    @时间：2021-03-18
    @说明：根据“configs/case_suite/case.aml”加载所有测试用例（三层结构）。
    参数：
    '''
    def get_case_suite(self):
        suite = unittest.TestSuite()
        #第一级为模块
        for module_key in case_suite_configs.get_cfg():
            module_name = module_root_dir + "." + module_key
            #动态加载模块
            __import__(module_name)
            class_section = case_suite_configs.get_cfg().get(module_key)
            for class_key in class_section:
                # 使用反射机制获取类
                clazz = getattr(sys.modules[module_name], class_key)
                # 遍历待测试的用例(方法)并加入测试套件中。
                func_names = class_section.get(class_key)
                if not func_names or not isinstance(func_names, list) or len(func_names) < 1:
                    continue
                for func_name in func_names:
                    # 判断是否使用了DDT驱动
                    cases = self.get_ddt_case(clazz, func_name)
                    for case in cases:
                        suite.addTest(clazz(case))
        return suite
    
    '''
    @作者：吴剑辉
    @时间：2021-03-19
    @说明：使用DDT驱动的用例必须以“test_”开头：否则不能被识别， 因为DDT会按照参数数据在后台生成新的用例名称
    '''
    def get_ddt_case(self, clazz, func_name:str):
        if not func_name:
            return[]
        if not func_name.upper().startswith("DDT:"):
            return [func_name]
        func_name = func_name.split(":")[1]
        cases = unittest.TestLoader().getTestCaseNames(clazz)
        cases = (case for case in cases if case.find(func_name) ==0 )
        return cases