import sys
import os
from flask import Flask, session

from src.views.mainview import mainview
from src.views.chatview import chatview


#sys.path.append(u"/home/dimkonko/env/FlaskBlog")

app = Flask(__name__)
app.debug = True
app.secret_key = os.urandom(27)

app.register_blueprint(mainview)
app.register_blueprint(chatview)
