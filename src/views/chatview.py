from flask import (Blueprint, render_template, request, redirect,
				   session)
from src.models.chatmodel import ChatModel

chatview = Blueprint("chatview", __name__,
					 template_folder="../templates")

model = ChatModel()

@chatview.route("/chat")
def chat():
	if 'username' in session:
		return render_template("chat.html",
							   nickname=session["username"])
	#return "You are not logged in"
	return redirect("/")
