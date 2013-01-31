import re, random, string
from model.Service import Service

class StringHelper(Service):
	articles = ["a", "an", "the", "of", "is"]

	def randomLetterString(self, numCharacters = 8):
		return "".join(random.choice(string.ascii_letters) for i in range(numCharacters))

	def tagsToTuple(self, tags):
		return tuple(self.titleCase(tag) for tag in tags.split(",") if tag.strip())

	def titleCase(self, s):
		wordList = s.split(" ")
		result = [wordList[0].capitalize()]

		for word in wordList[1:]:
			result.append(word in self.articles and word or word.capitalize())

		return " ".join(result)

	def validEmail(self, email):
		return re.match(r"[^@]+@[^@]+\.[^@]+", email)
		