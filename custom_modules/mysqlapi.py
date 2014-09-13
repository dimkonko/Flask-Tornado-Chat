import sqlite3

class MySqlApi(object):
	def conn(self):
		return sqlite3.connect("db/users.db")

	def add(self, sql_string):
		"""This function inserts data insto db
		"""
		conn = self.conn()
		cursor = conn.cursor()
		cursor.execute(sql_string)
		conn.commit()
		conn.close()
		return True

	def get(self, sql_string):
		"""This function gets data from db
		"""
		conn = self.conn()
		cursor = conn.cursor()
		cursor.execute(sql_string)
		data = cursor.fetchall()
		conn.close()
		return data