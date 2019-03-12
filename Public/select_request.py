# -*- coding: utf-8 -*-
from Public.requests import Rquest_Api
from Branch.log import Log
from Branch.operate_db import Operate_db
from config.readyaml import Getyaml

interface = Rquest_Api()
class TestApi(object):
	def __init__(self,url,key,param,way,place,assertdata):
		self.url = url
		self.key = key
		self.param = param
		self.way = way
		self.place = place
		self.assertdata = assertdata

	def get_param(self):
		if self.place != 'database':
			return self.param
		else:
			#获取数据库名
			self.database = Getyaml(yamlparam="interface_db",interface=self.url).port_db()
			Log().info('当前接口涉及数据库：%s' % self.database)
			#执行数据库操作
			post_data = Operate_db(self.database,self.url).Perform()
			Log().info('数据格式为：%s' % post_data)
			return post_data

	def selectway(self):
		if self.way == 'POST':
			#self.param = {'key': self.key, 'info': self.param}
			self.response = interface.post(self.url, self.get_param(), self.assertdata)
		elif self.way == "GET":
			self.parem = {'key': self.key, 'info': self.param}
			self.response = interface.get(self.url, self.get_param())
		elif self.way == "PUT":
			#self.param = {'key': self.key, 'info': self.param}
			self.response = interface.put(self.url, self.get_param(), self.assertdata)
		elif self.way == "DELETE":
			self.param = {'key': self.key, 'info': self.param}
			self.response = interface.delete(self.url, self.get_param())
		return self.response
	# def getJson(self):
	# 	json_data = self.testapi()
	# 	return json_data