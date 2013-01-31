import os
import beaker
from bottle import request
from beaker.middleware import SessionMiddleware

DEBUG = True
BIND_TO_OUTSIDE_IP = False
BIND_TO_PORT = 8080
ROOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "app")
RESOURCES_PATH = os.path.join(ROOT_PATH, "resources")
BASE_TEMPLATE_PATH = os.path.join(ROOT_PATH, "views")
SESSION_PATH = os.path.join(ROOT_PATH, "sessions")


ENV = "dev"

ENVIRONMENTS = {
	"dev": {
		"DBSERVER": "localhost",
		"DBUSER": "user",
		"DBPASS": "password"
	},
	"test": {
		"DBSERVER": "localhost",
		"DBUSER": "user",
		"DBPASS": "password"
	},
	"beta": {
		"DBSERVER": "localhost",
		"DBUSER": "user",
		"DBPASS": "password"
	},
	"demo": {
		"DBSERVER": "localhost",
		"DBUSER": "user",
		"DBPASS": "password"
	},
	"prod": {
		"DBSERVER": "localhost",
		"DBUSER": "user",
		"DBPASS": "password"
	},
}

DBNAME = "dbname"
DBSERVER = ENVIRONMENTS[ENV]["DBSERVER"]
DBUSER = ENVIRONMENTS[ENV]["DBUSER"]
DBPASS = ENVIRONMENTS[ENV]["DBPASS"]


#
# Session settings
#
SESSION_OPTS = {
	"session.type": "ext:database",
	"session.cookie_expires": 14400,
	"session.auto": True,
	"session.url": "mysql+mysqldb://{0}:{1}@{2}/{3}".format(DBUSER, DBPASS, DBSERVER, DBNAME),
	"session.table_name": "admin_session",
	"session.lock_dir": os.path.join(SESSION_PATH, "lock"),
	"session.data_dir": os.path.join(SESSION_PATH, "data")
}
