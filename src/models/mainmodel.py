from usermodel import UserModel

class MainModel(object):
	def __init__(self):
		self.user = UserModel()

	def add_user(self, user_form):
		print user_form["nickname"]
		print user_form["email"]
		print user_form["passwd"]
		a = self.user.add(nickname=user_form["nickname"],
			email=user_form["email"],
			password=user_form["passwd"])

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
