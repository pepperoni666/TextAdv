import items

class Character(object):
	def __init__(self, name):
		self.name = name
		self.loot = [items.Key("a")]
		pass