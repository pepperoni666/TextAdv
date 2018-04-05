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

	def hall(self, _input):
		if not symb[_input] == "#":
			if self.x.room(_input):
				return True;
		else:
			print "door is closed"
		return False;
	def rmenu(self, _input):
		if _input == "1":
			self.x.all();
		elif _input == "2":
			pass
		elif _input == "3":
			pass
		elif _input == "4":
			self.x.loot();
		elif _input == "5":
			pass
		else:
			pass
	def gameplay(self):
		while True: 
			_input = raw_input(">")
			_input = _input.lower()
			if _input in comm:
				self.rmenu(_input)
			elif _input in symb:
				if self.hall(_input):
					break;
			else:
				continue



g = game()
g.gameplay()