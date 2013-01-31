class DAO:
	db = None

	def __init__(self, db):
		self.db = db
		
	def escapeString(self, s):
		return self.db.connection.escape_string(s)

	def execute(self, sql, params = (), writeToConsole = False):
		rowsAffected = 0

		try:
			rowsAffected = self.db.execute(sql, params)

			if writeToConsole:
				print self.getLastExecuted()
				
		except Exception as e:
			print "An error occured in %s: %s" % (self, e)
			print "Last executed SQL:"
			print self.getLastExecuted()

			raise e

		return rowsAffected
		
	def executeMany(self, sql, paramArray = []):
		try:
			self.db.executemany(sql, paramArray)

		except Exception as e:
			print "An error occured in %s: %s" % (self, e.message)
			print "Last executed SQL:"
			print self.getLastExecuted()

			raise e
			
	def fetchAll(self):
		return self.db.fetchall()

	def fetchOne(self):
		return self.db.fetchone()

	def getLastExecuted(self):
		return self.db._last_executed

	def inject(self, key, value):
		self.__dict__[key] = value

	def lastRowId(self):
		return self.db.lastrowid