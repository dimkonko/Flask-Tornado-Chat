import MySQLdb as mdb

from ConfigLoader import ConfigLoader

class MySqlApi(object):
	def __init__(self):
		#config = ConfigLoader(sys.path[0] + "/conf/db_conf.ini").load()
		config = ConfigLoader("conf/db_conf.ini").load()
		self.host = config["host"]
		self.user = config["user"]
		self.passwd = config["passwd"]
		self.db = config["db"]

	def conn(self):
		return mdb.connect(host=self.host, user=self.user,
                   passwd=self.passwd, db=self.db)

	def add(self, sql_string):
		"""This function inserts data insto db
		"""
		db = self.conn()
		cursor = db.cursor()
		cursor.execute(sql_string)
		cursor.commit()
		db.close()
		return True

	def get(self, sql_string):
		"""This function gets data from db
		"""
		db = self.conn()
		cursor = db.cursor()
		cursor.execute(sql_string)
		data = cursor.fetchall()
		db.close()
		return data