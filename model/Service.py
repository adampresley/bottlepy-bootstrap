class Service:
	db = None

	def __init__(self, db):
		self.db = db

	def inject(self, key, value):
		self.__dict__[key] = value
				
