from bottle import view, route, request

@route("/")
@view("home")
def home():
	exampleService = request.factory.getExampleService()

	viewData = { "message": exampleService.getGreetingMessage("Adam Presley") }
	return viewData
