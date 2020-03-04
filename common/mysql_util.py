# -*- coding: utf-8 -*-

'''
1，连接数据库
2，编写sql脚本
3，创建游标
4，execute 运行
'''
import pymysql
from common.config import ConfigLoader

class MysqlUtil:
    def __init__(self):
        Config = ConfigLoader()
        host = Config.get("mysql", "host")
        user = Config.get("mysql", "user")
        password = Config.get("mysql", "pwd")
        port = Config.getint("mysql", "port")
        try:
            self.mysql = pymysql.connections.Connection(host=host, user=user, password=password, port=port,cursorclass=pymysql.cursors.DictCursor)
        except ConnectionError as e:
            raise e

    def fetch_one(self,sql):
        cursor = self.mysql.cursor()# 建立游标
        cursor.execute(sql)# 根据sql 进行查询
        return  cursor.fetchone() # 返回一条数据

    def fetct_all(self,sql):
        cursor = self.mysql.cursor()
        cursor.execute(sql)
        return cursor.fetchall()




