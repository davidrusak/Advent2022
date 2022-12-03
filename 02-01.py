def GetData(debug):
	
	if debug == True:
		file = open(puzzleNum + "-testdata.txt","r")
	else:
		file = open(puzzleNum + "-data.txt","r")
	lines = file.readlines()
	
	#sanitize all the /ns out
	for i in range(len(lines)):
		lineBreakIndex = lines[i].find("\n")
		if lineBreakIndex >= 0:
			lines[i] = lines[i][:lineBreakIndex]


	#get paired results
	pairs = []
	for i in range(len(lines)):
		pairs.append(lines[i].split())

	
	
	return pairs


rock = 0
paper = 1
scissors = 2

loss = 0
tie = 3
win = 6

def GetPlay(val):
	if val == "A":
		return rock
	elif val == "B":
		return paper
	elif val == "C":
		return scissors
	elif val == "X":
		return rock
	elif val == "Y":
		return paper
	elif val == "Z":
		return scissors
	else:
		print("WTF")
		return -1 

def GetRVictoryScore(l,r):
	if l == r:
		return tie
	elif l == rock:
		if r == scissors:
			return loss
		elif r == paper:
			return win
	elif l == paper:
		if r == scissors:
			return win
		elif r == rock:
			return loss
	elif l == scissors:
		if r == rock:
			return win
		elif r == paper:
			return loss
	else:
		print("WTF")
		return -1 
	

def GetPlayScore(r):
	return r + 1

def GetPairScore(l,r):
	lPlay = GetPlay(l)
	rPlay = GetPlay(r)
	return GetRVictoryScore(lPlay,rPlay) + GetPlayScore(rPlay)




################################################################

puzzleNum = "02"
debug = False


def main():
	pairs = GetData(debug)

	totalScore = 0
	for i in range(len(pairs)):
		totalScore += GetPairScore(pairs[i][0],pairs[i][1])

	print(totalScore)	
	
	
main()