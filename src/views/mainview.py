from flask import (Blueprint, render_template, request, redirect,
				   session)
from ..models.mainmodel import MainModel

mainview = Blueprint("mainview", __name__,
					 template_folder="../templates")

mainmodel = MainModel()

@mainview.route("/")
def index():
	isLogedIn = False
	if "username" in session:
		isLogedIn = True
	return render_template("index.html", isLogedIn=isLogedIn)

@mainview.route("/signup", methods=["POST"])
def signup():
	if request.method == "POST":
		mainmodel.add_user(request.form)
		return redirect("/")

@mainview.route("/login", methods=["POST"])
def login():
	user = mainmodel.get_user(request.form)
	if user:
		session["username"] = user["nickname"]
		return redirect("/chat")
	else:
		return "Wrong email or password"

@mainview.route("/logout")
def logout():
	session.pop("username", None)
	return redirect("/")
