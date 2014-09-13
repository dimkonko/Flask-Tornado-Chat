from custom_modules.mysqlapi import MySqlApi

class UserModel(object):
	def __init__(self):
		self.api = MySqlApi()
		self.fields = {
			"nickname": "nickname",
			"email": "email",
			"password": "password"
		}

	def add(self, nickname, email, password):
		sql = "INSERT INTO users(nickname, email, password) " +\
		      "VALUES('{0}', '{1}', '{2}');".format(
		            nickname,
		            email.encode("utf-8"),
		            password
		            )
		self.api.add(sql)
		return True

	def is_exists(self, nickname, email):
		sql = "SELECT nickname, email FROM users WHERE "+\
			  "nickname = '{0}' OR email = '{1}'".format(
					nickname, email)
		data = self.api.get(sql)
		
		if not data:
			return False
		else:
			return True

	def get(self, email):
		sql = "SELECT * FROM users WHERE email = '{0}'".format(
			email)
		user = self.api.get(sql)
		return user