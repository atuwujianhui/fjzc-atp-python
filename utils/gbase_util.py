#coding=utf-8

import os
import sys
root_path = os.getcwd()
sys.path.append(root_path)

import pymysql
from utils.init_file_util import IniFileUtil

class GbaseUtil():
    def __init_(self) -> None:
        #获取数据库配置信息
        ini_file_util = IniFileUtil(root_path + "/configs/database.ini")
        ip = ini_file_util.get_value ("gbase", "ip")
        port = int(ini_file_util.get_value("gbase", "port"))
        user_name = ini_file_util.get_value("gbase", "user_name")
        password = ini_file_util.get_value("gbase", "password")
        db = ini_file_util.get_value ("gbase", "db")
        charset = ini_file_util.get_value("gbase", "charset")
        #连接数据库
        self.conn = pymysql.connect(host = ip, 
            port = port, 
            user = user_name, 
            password = password, 
            db = db, 
            charset = charset
            #charset ="utf8mb 4”
        )

    def execute ( self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            return cur.fetchall()
        except Exception as e:
            # return e.args[1]
            print(sql)
            print(e)
        return None

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    pass