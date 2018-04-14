import abc
from dic import pos

class Condition(object):
	@abc.abstractmethod
	def __init__(self, C):
		self.comnds = []
		self.room = C;

	@abc.abstractmethod
	def conditInput(self, player, input):
		pass

class introCondit(Condition):
	def __init__(self, C):
		super(introCondit, self).__init__(C)
		self.comnds.append("ok")
	def conditInput(self, player, input):
		if input == "ok":
			return 1

class okCondit(Condition):
	def __init__(self, C):
		super(okCondit, self).__init__(C)
		self.comnds.append("ok")
	def conditInput(self, player, input):
		if input == "ok":
			pos[self.room] = pos[self.room] + 1
			return 2

class endCondit(Condition):
	def __init__(self, C):
		super(endCondit, self).__init__(C)
		self.comnds.append("back")
	def conditInput(self, player, input):
		if input == "back":
			return 1