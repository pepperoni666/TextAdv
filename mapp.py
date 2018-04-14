import os, items, reader
from dic import symb, comm
from characters import Character

class map(object):
	def __init__(self):
		os.system("clear")
		self.inRoom = True
		self.player = Character("player")
		self.R = -1
		self.condit = reader.readRoom("txtStory/intro.txt", self.R)
		self.printCondit()
	def printCondit(self):
		print "\n"
		for i in range(len(self.condit.comnds)):
			print "%d) %s" %(i+1, self.condit.comnds[i])
		print "\n"
	def input(self, _input):
		if self.inRoom:
			if _input == "l":
				self.loot()
				return False
			resp = self.condit.conditInput(self.player, self.condit.comnds[int(_input)-1])
			if resp == 1:
				self.all()
			elif resp == 0:
				print "discard"
			elif resp == 2:
				if self.room(self.R):
					return True
			else:
				pass

		else:
			if not symb[_input] == "#":
				if self.room(_input):
					return True
			else:
				print "door is closed"
			return False
	def all(self):
		self.R = ""
		self.inRoom = False
		for i in symb.keys():
			symb[i] = "#"
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
		self.R = C
		self.inRoom = True
		os.system("clear")
		if C == "exit":
			print "bye"
			return True
		print "==============%s==============\n" %C.upper()
		file = "txtStory/room" + C + ".txt"
		self.condit = reader.readRoom(file, C)
		self.printCondit()
		return False

	def loot(self):
		if(len(self.player.loot)==0):
			print "Empty"
		else:
			for i in self.player.loot:
				print i.name
		return False