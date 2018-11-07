# -*- coding: utf-8 -*-
from Public.requests import requ
from config.readyaml import Getyaml
from Public.log import Log
from Public.operate_db import Operate_db

reques=requ()
class TestApi(object):
	def __init__(self,url,key,connent,fangshi,param_place,assertdata):
		self.url = url
		self.key = key
		self.connent = connent
		self.fangshi = fangshi
		self.param_place = param_place
		self.assertdata = assertdata

	def get_param(self):
		if self.param_place != 'database':
			return self.connent
		else:
			#获取数据库名
			self.database = Getyaml(yamlparam="interface_db",interface=self.url).port_db()
			Log().info('当前接口涉及数据库：%s' % self.database)
			#执行数据库操作
			post_data = Operate_db(self.database,self.url).Perform()
			Log().info('数据格式为：%s' % post_data)
			return post_data

	def testapi(self):
		if self.fangshi=='POST':
			#self.parem = {'key': self.key, 'info': self.connent}
			self.response=reques.post(self.url, self.get_param(), self.assertdata)
		elif self.fangshi=="GET":
			self.parem = {'key': self.key, 'info': self.connent}
			self.response = reques.get(self.url, self.get_param())
		elif self.fangshi == "PUT":
			#self.parem = {'key': self.key, 'info': self.connent}
			self.response = reques.putfile(self.url, self.get_param(), self.assertdata)
		elif self.fangshi == "DELETE":
			self.parem = {'key': self.key, 'info': self.connent}
			self.response = reques.delfile(self.url, self.get_param())
		return self.response
	# def getJson(self):
	# 	json_data = self.testapi()
	# 	return json_data