import bottle, config, re, MySQLdb
import MySQLdb.cursors as cursors
from bottle import request, response, redirect

from model.Factory import Factory

def preRequest(callback):
	def wrapper(*args, **kwargs):
		#
		# Setup session and environment stuff
		#
		request.session = request.environ.get("beaker.session")
		request.all = dict(request.query.items() + request.forms.items())

		# 
		# Setup database object. Uncomment lines 19-24, 37-38 and comment line 25 to 
		# enable MySQL
		#
		# request.dbConnection = MySQLdb.connect(config.DBSERVER, config.DBUSER, config.DBPASS, config.DBNAME, cursorclass = cursors.DictCursor, charset = "utf8", port = 3306)
		# request.db = request.dbConnection.cursor()
		
		# request.db.execute("set time_zone=%s", ("+0:00",))
		# request.db.close()
		# request.db = request.dbConnection.cursor()
		request.db = None

		request.factory = Factory(request.db)

		# 
		# Finally call the the next method in the chain
		#
		body = callback(*args, **kwargs)

		#
		# Commit and close db connection
		#
		# request.dbConnection.commit()
		# request.dbConnection.close()

		return body

	return wrapper
