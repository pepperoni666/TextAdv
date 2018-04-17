from dic import pos, choices
import conditions

def readRoom(FileName, C=-1):
	if C is not -1:
		if C in choices:
			FileName = "txtStory/choose" + C*choices[C] + ".txt"
			C *= (choices[C]+1)
	with open(FileName, "r") as f:
		if C is not -1:
			for i in range(pos[C]):
				stmp = f.readline()
				while "|" not in stmp:
					stmp = f.readline()
		while True:
			stmp = f.readline()
			if "|" in stmp:
				print stmp.rpartition('|')[0]
				if stmp.rpartition('|')[2].split('\n')[0].split(' ')[0].lower() == "chooseend":
					pos[C] +=1
					continue
				return readCondit(stmp.rpartition('|')[2], C)
			else:
				print stmp
	print "\n"

def skip(FileName, C):
	with open(FileName, "r") as f:
		for i in range(pos[C]):
			stmp = f.readline()
			while "|" not in stmp:
				stmp = f.readline()
		while True:
			stmp = f.readline()
			if "|chooseend" in stmp.lower():
				pos[C] += 1
				break
			elif "|" in stmp:
				pos[C] += 1

def readCondit(str, C):
	args = str.split('\n')[0].split(' ')
	if args[0].lower() == "ok":
		return conditions.okCondit(C)
	elif args[0].lower() == "intro":
		return conditions.introCondit(C)
	elif args[0].lower() == "end":
		if C[0] in choices:
			if choices[C[0]]==1:
				del choices[C[0]]
				del pos[C]
				skip("txtStory/room" + C[0] + ".txt", C[0])
				return readRoom("txtStory/room" + C[0] + ".txt", C[0])
			del pos[C]
			choices[C[0]] -= 1
			skip("txtStory/choose" + C[:len(C)-2] + ".txt", C[:len(C)-1])
			return readRoom("txtStory/choose" + C[:len(C)-2] + ".txt", C[:len(C)-1])
		return conditions.endCondit(C)
	elif args[0].lower() == "take":
		return conditions.takeCondit(C, args[1].lower(), args[2].lower())
	elif args[0].lower() == "give":
		return conditions.giveCondit(C, args[1].lower(), args[2].lower())
	elif args[0].lower() == "choose":
		return conditions.chooseCondit(C, args[1], args[2])
	else:
		return conditions.endCondit(C)