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



def gameplay(x):
	while True: 
		_input = raw_input(">")
		_input = _input.lower()
		if _input in comm:
			if _input == "1":
				x.all();
			elif _input == "2":
				pass
			elif _input == "3":
				pass
			elif _input == "4":
				x.loot();
			elif _input == "5":
				pass
			else:
				pass
		elif _input in symb:
			if not symb[_input] == "#":
				if x.room(_input):
					break;
			else:
				print "door is closed"
		else:
			continue



x = map()
gameplay(x)