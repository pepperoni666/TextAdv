from dic import pos
import conditions

def readRoom(FileName, C=-1):
	with open(FileName, "r") as f:
		if(C != -1):
			for i in range(pos[C]):
				stmp = f.readline()
				while "|" not in stmp:
					stmp = f.readline()
		while True:
			stmp = f.readline()
			if "|" in stmp:
				print stmp.rpartition('|')[0]
				return readCondit(stmp.rpartition('|')[2])
			else:
				print stmp
	print "\n"

def readCondit(str):
	args = str.split(' ')
	if(args[0].lower() == "ok"):
		return conditions.okCondit()
	else:
		return conditions.intoCondit()