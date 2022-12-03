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
	groups = []
	for i in range(0,len(lines),3):
		groups.append([lines[i],lines[i+1],lines[i+2]])
		
	
	return groups

def GetCommonLetter(chunk1, chunk2, chunk3):
	for letter in chunk1:
		if letter in chunk2:
			if letter in chunk3:
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
	groups = GetData(debug)
	for group in groups:
		sum += GetPrio(GetCommonLetter(group[0],group[1],group[2]))
	print(sum)
	
	
main()