import sqlite3

db = "db/users.db"
sql1 = "DROP TABLE IF EXISTS users"
sql = open('db/db.sql', 'r').read()
print sql

conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute(sql1)
cur.execute(sql)
conn.commit()
conn.close()