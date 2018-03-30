class Item(object):
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return "{}\n--{}\nValue: {}".format(self.name, self.description, self.value)


class Key(Item):
	def __init__(self, lock):
		self.lock = lock
		super(Key, self).__init__("Key", "Old-style, long, metal key, with a note on it. The note says: \"{}\"".format(self.lock), self.lock)


class Tool(Item):
	def __init__(self, name, description, value):
		super(Tool, self).__init__(name, description, value)