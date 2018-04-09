from mapp import map
from dic import symb, comm
"""from sys import platform

if platform == "linux" or platform == "linux2":
	print "linux"
elif platform == "win32":
	print "win32"
elif platform == "win64":
	print "win64"
"""


class game(object):
	def __init__(self):
		self.x = map()
	def gameplay(self):
		while True: 
			_input = raw_input(">")
			_input = _input.lower()
			if self.x.input(_input):
				break



g = game()
g.gameplay()