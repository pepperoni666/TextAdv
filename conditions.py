import abc

class Condition(object):
	@abc.abstractmethod
	def test(self):
		pass

class intoCondrit(Condition):
	def test(self):
		pass