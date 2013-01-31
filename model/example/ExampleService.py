from model.Service import Service

class ExampleService(Service):
	def getGreetingMessage(self, name):
		return "Hello %s. Greetings to you!" % name

	def getTwoPlusTwo(self):
		return 2 + 2
		