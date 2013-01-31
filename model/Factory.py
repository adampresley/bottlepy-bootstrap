from model.DateHelper import DateHelper
from model.example.ExampleService import ExampleService
from model.StringHelper import StringHelper

class Factory:
	db = None

	def __init__(self, db):
		self.db = db

	def getDateHelper(self):
		return self._getService(DateHelper(self.db), [])

	def getExampleService(self):
		return self._getService(ExampleService(self.db), [])
		
	def getStringHelper(self):
		return self._getService(StringHelper(self.db), [])
		

	def _getService(self, service, stuff):
		for item in stuff:
			service.inject(item[0], item[1])

		return service

	def _getDAO(self, dao):
		dao.inject("dateHelper", self.getDateHelper())
		return dao
