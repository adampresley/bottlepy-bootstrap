import unittest, os, sys
from mock import Mock, MagicMock

sys.path.insert(1, "../")

from model.example.ExampleService import ExampleService

class TestExampleService(unittest.TestCase):
	def setUp(self):
		self.exampleService = ExampleService(None)


	def test_getGreetingMessage_WithNameAdam_ReturnsStringWithNameAdam(self):
		expected = "Hello Adam. Greetings to you!"
		actual = self.exampleService.getGreetingMessage(name = "Adam")

		self.assertEqual(expected, actual, "The expected string did not come back")

	def test_getTwoPlusTwo_Returns4(self):
		expected = 4
		actual = self.exampleService.getTwoPlusTwo()

		self.assertEqual(expected, actual, "Expected 2 + 2 to equal 4")
		