import sys, os
from datetime import datetime
from socket import socket, SOCK_DGRAM, AF_INET

#
# Add current and parent path to syspath
#
currentPath = os.path.dirname(__file__)
parentPath = os.path.abspath(os.path.join(currentPath, os.path.pardir))

paths = [
	currentPath,
	parentPath
]

for path in paths:
	if path not in sys.path:
		sys.path.insert(0, path)

os.chdir(currentPath)


#
# Import framework and controllers
#
import config, bottle
import bottle_preRequest
from beaker.middleware import SessionMiddleware

from bottle import route, run, view
from bottle import TEMPLATE_PATH, request, static_file
from bottle import install

# Import all of your controllers here...
from app.controllers import home


#
# Add view paths to the Bottle template path
#
TEMPLATE_SUB_PATHS = os.walk(config.BASE_TEMPLATE_PATH).next()[1]
bottle.TEMPLATE_PATH.append(config.BASE_TEMPLATE_PATH)

for templatePath in TEMPLATE_SUB_PATHS:
	bottle.TEMPLATE_PATH.append(os.path.join(config.BASE_TEMPLATE_PATH, templatePath))


if config.DEBUG:
	print "ROOT_PATH: %s" % config.ROOT_PATH
	print "Session path: %s" % config.SESSION_PATH
	print "Template Paths:"

	for it in bottle.TEMPLATE_PATH:
		print "   %s" % it

	print ""

	print "System paths:"
	for it in paths:
		print "   %s" % it

	print "\n%s\n" % datetime.today()


#
# Setup our pre-request plugin, session, debug mode, and methods
# to serve static resources.
#
install(bottle_preRequest.preRequest)
bottle.debug(config.DEBUG)

@route("/resources/<filepath:path>")
def serve_static(filepath):
	return static_file(filepath, root = config.RESOURCES_PATH)

@route("/heartbeat", method = "GET")
def heartbeat():
	return "A-OK ya'll!"

#
# Uncomment line 84 and comment line 83 to enable session management
#
app = bottle.app()
#app = SessionMiddleware(bottle.app(), config.SESSION_OPTS)

if config.BIND_TO_OUTSIDE_IP:
	_s = socket(AF_INET, SOCK_DGRAM)
	_s.connect(("google.com", 0))
	outsideIP = _s.getsockname()

if config.DEBUG:
	if config.BIND_TO_OUTSIDE_IP:
		run(app = app, host = outsideIP[0], port = config.BIND_TO_PORT, reloader = True)
	else:
		run(app = app, host = "localhost", port = config.BIND_TO_PORT, reloader = True)
else:
	if config.BIND_TO_OUTSIDE_IP:
		run(app = app, host = outsideIP[0], port = config.BIND_TO_PORT, server="gunicorn", workers = 4, proc_name = "APP", pidfile = "/tmp/app-gunicorn", daemon = True)
	else:
		run(app = app, host = "localhost", port = config.BIND_TO_PORT, server="gunicorn", workers = 4, proc_name = "APP", pidfile = "/tmp/app-gunicorn", daemon = True)


