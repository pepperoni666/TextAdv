import os, items, reader
from dic import symb, comm
from characters import Character

class map(object):
	def __init__(self):
		os.system("clear")
		self.player = Character("player");
		reader.readOnly("intro.txt")
		print "%s) %s" %("1", comm["2"])
	def all(self):
		for i in self.player.loot:
			if type(i) is items.Key:
				for key, val in symb.items():
					if i.lock == key:
						symb[key] = " "
		os.system("clear")
		print "\n\t\tExit%s" %symb["exit"]
		print "\t\t |"
		print "\tA%s-------+-------%sB" %(symb["a"], symb["b"])
		print "\t\t |"
		print "\tC%s-------+-------%sD" %(symb["c"], symb["d"])
		print "\t\t |"
		print "\t\t E%s\n" %symb["e"]

	def room(self, C):
		os.system("clear")
		if C == "exit":
			print "bye"
			return True
		print "==============%s==============\n" %C.upper()
		file = "room" + C + ".txt"
		reader.readRoom(file, C)
		for i in range(len(comm)):
			print "%d) %s" %(i+1, comm[str(i+1)])
		return False

	def loot(self):
		if(len(self.player.loot)==0):
			print "Empty"
		else:
			for i in self.player.loot:
				print i.name
		return False