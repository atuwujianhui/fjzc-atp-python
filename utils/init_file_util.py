#coding=utf-8

import configparser
import os
'''
@作者：吴剑辉
@时间：2020-11-30
@说明：ini配置文件工具类
'''

import os

class IniFileUtil(object):

    def __init__(self, file_name):
        try:
            self.cf = configparser.ConfigParser()
            # 解决ini文件中文编码问题
            self.cf.read(file_name, encoding = "utf-8-sig")
        except Exception as e:
            print(e)
            self.cf = None
    #取值
    def get_value(self, node, key):
        if not self.cf:
            return None
        return self.cf.get(node, key)

if __name__ == "__main__":
    ini_file_util = IniFileUtil(os.getcwd() + "/configs/config.ini")
    print(ini_file_util.get_value("system", "name"))
