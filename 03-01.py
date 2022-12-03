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
	bags = []
	for i in range(len(lines)):
		halfLength = len(lines[i]) // 2
		bags.append([lines[i][:halfLength], lines[i][halfLength:]])

	
	
	return bags

def GetCommonLetter(chunk1, chunk2):
	for letter in chunk1:
		if letter in chunk2:
			return letter
	
	print("WTF")
	return "WTF"

def GetPrio(val):
	if(val.islower()):
		return ord(val) - 96
	else:
		return ord(val) - 38


################################################################

puzzleNum = "03"
debug = False


def main():

	sum = 0
	bags = GetData(debug)
	for i in range (len(bags)):
		sum += GetPrio(GetCommonLetter(bags[i][0],bags[i][1]))

	print(sum)
	
	
main()