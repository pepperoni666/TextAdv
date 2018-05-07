import abc, items
from dic import pos, choices

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
		self.comnds.append("back")
	def conditInput(self, player, input):
		if input == "ok":
			pos[self.room] += 1
			return 2
		if input == "back":
			return 1

class endCondit(Condition):
	def __init__(self, C):
		super(endCondit, self).__init__(C)
		self.comnds.append("back")
	def conditInput(self, player, input):
		if input == "back":
			return 1

class takeCondit(Condition):
	def __init__(self, C, _item, _args):
		super(takeCondit, self).__init__(C)
		self.item = _item
		self.args = _args.split(',')
		self.comnds.append("ok   +1 item")
		self.comnds.append("back")
	def conditInput(self, player, input):
		if input == "ok   +1 item":
			if self.item == "key":
				player.loot.append(items.Key(self.args[0]))
			pos[self.room] += 1
			return 2
		if input == "back":
			return 1

class giveCondit(Condition):
	def __init__(self, C, _item, _args):
		super(giveCondit, self).__init__(C)
		self.item = _item
		self.args = _args.split(',')
		self.comnds.append("ok   -1 item")
		self.comnds.append("back")
	def conditInput(self, player, input):
		if input == "ok   -1 item":
			for x in player.loot:
				if self.item == x.name.lower():
					if self.item == "key":
						if self.args[0] == x.lock:
							player.loot.remove(x)
							pos[self.room] += 1
							return 2
			return 0
		if input == "back":
			return 1

class chooseCondit(Condition):
	def __init__(self, C, good, bad):
		super(chooseCondit, self).__init__(C)
		self.good = good
		self.bad = bad
		self.comnds.append(good)
		self.comnds.append(bad)
		self.comnds.append("back")
	def conditInput(self, player, input):
		if input == self.good:
			if self.room[0] in choices:
				choices[self.room[0]] += 1 
			else:
				choices[self.room[0]] = 1
			if self.room[0]*(choices[self.room[0]]+1) in pos.keys():
				pos[self.room[0]*(choices[self.room[0]]+1)] += 1
			else:
				pos[self.room[0]*(choices[self.room[0]]+1)] = 0
			return 2
		if input == self.bad:
			pos[self.room] += 1
			return 2
		if input == "back":
			return 1