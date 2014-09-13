import MySQLdb as mdb

from usermodel import UserModel

class MainModel(object):
	def __init__(self):
		self.user = UserModel()

	def add_user(self, user_form):
		self.user.add(user_form["nickname"],
			user_form["email"],
			user_form["password"])		

	def get_user(self, login_form):
		data = self.user.get(email=login_form["login"])

		if not data:
			return False

		user = data[0]
		# print "Login data:"
		# print user

		user_dict = {
			"nickname": user[0],
			"password": user[1]
		}

		if user_dict["password"] == login_form["passwd"]:
			return user_dict
		else:
			return False
