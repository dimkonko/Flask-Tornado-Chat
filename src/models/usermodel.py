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

	def get(self, nickname=None, email=None):
		if nickname:
			field = self.fields["nickname"]
			data = nickname
		else:
			field = self.fields["email"]
			data = email

		sql = "SELECT nickname, password FROM users WHERE {0} = '{1}'".format(
			field, data)
		user = self.api.get(sql)
		return user