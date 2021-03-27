#coding=utf-8

import cx_Oracle as cxo

class OracleUtil:

    def __init__(self, user_name, password, tns):
        self.user_name = user_name
        self.password = password
        self.tns = tns
        self.conn = None
        self.connect()
    def connect (self):
        if not self.conn:
            self.conn = cxo.connect(self.user_name, self.password, self.tns)
        else:
            pass

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def create_cursor(self):
        cur = self.conn.cursor()
        if cur:
            return cur
        else:
            print("游标创建失败！")
        return None

    def close_cursor (self, cur):
        if cur:
            cur.close()
            cur = None
    def export(self, sql, file_name, colfg = '||'):
        rt = self.query(sql)
        if rt:
            with open(file_name, 'a') as fd:
                for row in rt:
                    ln_info = ""
                    for col in row:
                        ln_info += str(col) + colfg
                    ln_info += "\n"
                    fd.write(ln_info)

    def query(self, sql, start = 0, num = -1):
        rt = []
        # 获取cursor
        cur = self.create_cursor()
        if not cur:
            return rt
        # 查询到列表
        cur.execute(sql)
        if(start == 0)and(num == 1):
            rt.append(cur.fetchone())
        else:
            rs = cur.fetchall()
        if num == -1:
            rt.extend(rs[start:] )
        else:
            rt.extend(rs[start: start + num] )
        #释放cursor
        self.close_cursor(cur)
        return rt

    # 待完善
    def exec_sql(self, sql):
        #获取cursor
        rt = None
        cur = self.create_cursor ()
        if not cur:
            return rt
        #判断sql是否允许其执行
        if not self.permited_update_sql(sql):
            return rt
        #执行语句
        rt = cur.execute(sql)
        #释放cursor
        self.close_cursor(cur)
        return rt
