import abc

class Condition(object):
	@abc.abstractmethod
	def __init__(self):
		self.comnds = []

	@abc.abstractmethod
	def test(self):
		pass

class intoCondit(Condition):
	def __init__(self):
		super(intoCondit, self).__init__()
	def test(self):
		pass

class okCondit(Condition):
	def __init__(self):
		super(okCondit, self).__init__()
		self.comnds.append("ok")
	def test(self):
		pass