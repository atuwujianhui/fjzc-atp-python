#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者：吴剑辉（福建中测）
# 时间：2021-03-20 09:22:26
# 文件名：yaml_file_util.py
# 说明：

import os
import sys
root_path = os.getcwd()
sys.path.append(root_path)
import yaml

class YamlFileUtil():
    
    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-20
    @ 说明：初始化加载yaml文件
    @ 参数：
    '''
    def __init__(self, yaml_file):
        with open(yaml_file, 'r', encoding = 'utf-8') as f:
            self.cfg = yaml.load(f.read(), Loader = yaml.FullLoader)

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-20
    @ 说明：获取yaml文件的内容
    @ 参数：
    '''
    def get_cfg(self):
        return self.cfg

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-20
    @ 说明：获取配置项
    @ 参数：
    '''
    def get_value(self, node_path):
        current_node = None
        nodes = node_path.split(".")
        if not nodes or len(nodes) < 1:
            return None
        for node in nodes:
            current_node = (current_node if current_node else self.cfg).get(node)
        return current_node

# 用例套件配置（单例模式）
case_suite_configs = YamlFileUtil(os.path.join(root_path, "configs/case_suite/case.yaml"))
# 元素定位信息配置（单例模式）
web_ui_element_configs = YamlFileUtil(os.path.join(root_path, "configs/web_ui/elements.yaml"))
# 系统全局配置（单例模式）
global_configs = YamlFileUtil(os.path.join(root_path, "configs/global_configs.yaml"))

'''
@ 作者：吴剑辉（福建中测）
@ 时间：2021-03-20
@ 说明：测试
@ 参数：
'''
if __name__ == "__main__":
    print(global_configs.get_value("system.find_element_timeout_default"))