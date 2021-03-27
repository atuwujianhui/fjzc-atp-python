#coding=utf-8

import os
import sys
from unittest import main
root_path = os.getcwd()
sys.path.append(root_path)
from utils.yaml_file_util import web_ui_element_configs
from utils.yaml_file_util import global_configs
from utils.yaml_file_util import YamlFileUtil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import re

_METHOD_ = {
    "ID": By.ID,
    "NAME": By.NAME,
    "XPATH": By.XPATH,
    "CLASS": By.CLASS_NAME,
    "TAG": By.TAG_NAME,
    "CSS": By.CSS_SELECTOR
}

class WebElementUtil():
    def __init__(self, driver, element_conf_file = None):
        self.driver = driver
        if not element_conf_file:
            self.web_ui_element_configs = web_ui_element_configs
        else:
            self.web_ui_element_configs = YamlFileUtil(root_path + "/configs/web_ui/element.yaml")
    
    def get_driver(self) -> webdriver:
        return self.driver

    def get_element(self, element_path, timeout = global_configs.get_value("system.find_element_timeout_default")):
        # 获取元素定位信息
        element_info = self.web_ui_element_configs.get_value(element_path)

        # 判断定位信息格式是否正确
        if not element_info:
            return None

        # 最终定位的元素
        element = None
        items = element_info.split(">>")
        # 根据配置文件进行元素的层层钻取定位
        for item in items:
            # 判断是否需要切换iFrame，列表数量超过1，表示前面需要切换iFrame
            sections = item.split("&&")
            if sections and type(sections) == list and len(sections) >1:
                #处理iFrams数组，数组最后一个为元素，所以要剔除
                for i in range(0, len(sections) - 1) :
                    element_info = self.split_element_info(sections[i] )
                if not element_info:
                    continue
                iframe_element = self.get_element_until_it_shows(element_info, element, timeout )
                self.driver.switch_to.frame(iframe_element)
            #获取元素对象
            element_info = self.split_element_info(sections[len(sections) - 1])
            if not element_info:
                return None
            element = self.get_element_until_it_shows(element_info, element, timeout)

            '''
            # 使用反射获取方法对象
            method = getattr(element if element else self.driver, method_name )
            element = method(element_name)
            '''

        self.driver.switch_to.default_content()
        return element

    def get_element_until_it_shows(self, element_info, parent_element = None, 
            timeout = global_configs.get_value("system.find_element_timeout_default")) :
        try:
            if parent_element:
                #查找父元素下的子元素无法使用等待加载超时功能
                return parent_element.find_elements(element_info[0], element_info[1] ) [element_info[2] ]
            else:
                return WebDriverWait(self.driver, timeout ).until(
                    EC.visibility_of_all_elements_located((element_info[0], element_info[1] ))
                )[element_info[2]]
        except Exception as e:
            print(e)
        return None

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-20
    @ 说明：拆分元素配置子节点信息
    @ 参数：
    '''
    def split_element_info(Self, section):
        index = 0
        result = re.findall(".+\(([0-9]+)\)", section)
        if result and len(result) > 0:
            index = int(result[0])
        result = re.sub("\(([0-9]+)\)", "", section)
        infos = result.split("::")
        if not infos or len(infos) <2 or not infos[0] or not infos[1]:
            return None
        #获取待调用的Driver方法名
        method_name = _METHOD_[infos[0].upper()]
        if not method_name:
            return None
        #获取元素名
        element_name = infos[1]
        return method_name, element_name, index

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-20
    @ 说明：文本输入
    @ 参数：
    '''
    def send_keys(self, element_path,value,
            timeout = global_configs.get_value("system.find_element_timeout_default")):
        try:
            element = self.get_element(element_path, timeout)
            element.send_keys(value)
        except Exception as e:
            print(e)

    '''
    @ 作者：吴剑辉（福建中测）
    @ 时间：2021-03-20
    @ 说明：点击
    @ 参数：
    '''
    def click(self, element_path,
            timeout = global_configs.get_value("system.find_element_timeout_default")):
        try:
            element = self.get_element(element_path, timeout)
            element.click()
        except Exception as e:
            print(e)

'''
@ 作者：吴剑辉（福建中测）
@ 时间：2021-03-20
@ 说明：测试
@ 参数：
'''
if __name__ == "__main__":
    result = re.findall(".+\(([0-9]+)\)", "name::email(0)")
    result = re.findall(".+\(([0-9]+)\)", "name::email")
    print(result)