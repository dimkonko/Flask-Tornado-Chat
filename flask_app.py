import sys
import os
import sqlite3
from flask import Flask, session

from src.views.mainview import mainview
from src.views.chatview import chatview
from custom_modules.mysqlapi import MySqlApi


DATABASE = "db/users.db"
#Init db
db = "db/users.db"
sql1 = "DROP TABLE IF EXISTS users"
sql = open('db/db.sql', 'r').read()

conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute(sql1)
cur.execute(sql)
conn.commit()
conn.close()
print "Database created";
#sys.path.append(u"/home/dimkonko/env/FlaskBlog")

app = Flask(__name__)
app.debug = True
app.secret_key = os.urandom(27)

app.register_blueprint(mainview)
app.register_blueprint(chatview)


