#!/user/bin/env python
# encoding: utf-8
# @author: renchuang
# @file: pymsql_utils.py
# @time: 2021/6/28 下午8:51

import pymysql

class PymsqlUtils(object):
	def __init__(self):
		self.config = {
		'host':'47.101.137.66',
		'user':'root',
		'password':'123456',
		'db':'mysql_practice',
		'charset':'utf8'
	}
	def select_sql(self,sql):
		db = pymysql.connect(**self.config)
		
		with db.cursor(pymysql.cursors.DictCursor) as cur:
			try:
				# sql = 'select * from student'
				cur.execute(sql)
				response = cur.fetchall()
				# print(response)
			except Exception as err:
				print("sql执行错误，原因：",err)
				
		db.close()
		return response
py = PymsqlUtils()
if __name__ == '__main__':
	py = PymsqlUtils()
	sql = 'select * from student'
	py.select_sql(sql)