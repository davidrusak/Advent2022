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

	return lines

def PrintUniqueStringIndex(data, markerLength):
	for stream in data:
		marker = []
		for i in range (len(stream)):
			marker.append(stream[i])
			if len(marker) > markerLength:
				marker.pop(0)
			# print("".join(marker))
			
			allUnique = len(marker) >= markerLength
			for num in marker:
				if marker.count(num) != 1:
					allUnique = False
			if allUnique == True:
				#the answer wants 1-based counting so add 1
				print(i + 1)
				break

################################################################

puzzleNum = "06"
debug = False


def main():
	
	data = GetData(False)

	print("06.01: ")
	PrintUniqueStringIndex(data, 4)

	print("06.02: ")
	PrintUniqueStringIndex(data, 14)

	

	# print(marker)
	
	
main()