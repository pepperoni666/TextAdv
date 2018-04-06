from dic import pos

def readOnly(FileName):
	with open(FileName, "r") as f:
		while True:
			stmp = f.readline()
			if "|" in stmp:
				print stmp.rpartition('|')[0]
				break
			else:
				print stmp
	print "\n"

def readRoom(FileName, C):
	with open(FileName, "r") as f:
		for i in range(pos[C]):
			stmp = f.readline()
			while "|" not in stmp:
				stmp = f.readline()
		while True:
			stmp = f.readline()
			if "|" in stmp:
				print stmp.rpartition('|')[0]
				readCondit(stmp.rpartition('|')[1])
				break
			else:
				print stmp
	print "\n"

def readCondit(str):
	args = str.split(' ')
	if(args[0] == "end"):
		pass
	else:
		pass