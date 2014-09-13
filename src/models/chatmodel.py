from usermodel import UserModel

class ChatModel(object):
	def __init__(self):
		self.user = UserModel()

	def get_user(self, nickname):
		self.user.get(nickname=nickname)
