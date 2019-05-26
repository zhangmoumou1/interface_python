#Author:命命
#coding=utf-8
import os
import pymysql
from Branch.log import Log
from config.readyaml import Getyaml
import redis

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(curPath, "db.yaml")

class Operate_db():

    def __init__(self,getdb,interface_url):
        self.getdb = getdb
        self.interface_url = interface_url

    def connect_db(self):
        self.getdb1 = Getyaml(yamlparam=self.getdb,interface='interface').get_data()
        db1 = pymysql.connect(self.getdb1[0], self.getdb1[1], self.getdb1[2], self.getdb1[3],charset='utf8')
        return db1

    def get_sql(self):
        self.sql = Getyaml(yamlparam="interface_sql",interface='interface').get_data()
        for key, value in self.sql.items():
            if key == self.interface_url:
                return value

    def Perform(self):
        # 使用cursor()方法获取操作游标
        self.db = self.connect_db()
        self.cursor = self.db.cursor()
        sql = self.get_sql()
        version = self.db.server_version
        Log().info('成功登录数据库：%s，版本为：%s，执行SQL：%s' % (self.getdb, version, sql))
        if "SELECT" in sql or "select" in sql:
            try:
                self.cursor.execute(sql)
                results = self.cursor.fetchall()
                Log().info('查询结果：%s' % results[0][0])
                return results[0][0]
            except:
                Log().info("Error: unable to fetch data")
                raise
        elif "UPDATE" in sql or "update" in sql:
            try:
                self.cursor.execute(sql)
                self.db.commit()
                Log().info("更新成功")
            except:
                self.db.rollback()
                Log().info("Error：Has been rolled back")
                raise
        self.db.close()


class Operate_redis():

    def connect(self):
        r = redis.Redis(host='116.62.201.163', port=6379, password='123456', db=1)
        r.set('name', 'root')
        print(r.get('name').decode('utf8'))

# interface_url = "http://127.0.0.1:5000/todos/todo2"
# getdb = "orderdb"
# Operate_db(getdb,interface_url).Perform()

Operate_redis().connect()