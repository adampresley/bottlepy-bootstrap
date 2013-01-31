from bottle import response

def error(message):
	response.status = 500
	return message

def notFound():
	response.status = 404
	return "Resource not found"