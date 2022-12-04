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
	for line in lines:
		unexpandedPair = line.split(",")
		expandedPair = [unexpandedPair[0].split("-"),unexpandedPair[1].split("-")]
		expandedPair = [[int(expandedPair[0][0]), int(expandedPair[0][1])],[int(expandedPair[1][0]), int(expandedPair[1][1])]]
		pairs.append(expandedPair)

	
	
	return pairs



################################################################

puzzleNum = "04"
debug = False


def main():

	count = 0
	pairs = GetData(debug)
	for pair in pairs:

		#0 contains 1
		# if (pair[0][0] <= pair[1][0]) & (pair[0][1] >= pair[1][1]):
			
		#0 overlaps 1 from below
		if (pair[0][0] <= pair[1][0]) & (pair[0][1] >= pair[1][0]) :
			count += 1

		#0 overlaps 1 from above
		elif (pair[1][0] <= pair[0][0]) & (pair[1][1] >= pair[0][0]):
			count += 1

		#1 contains 0
		# elif (pair[1][0] <= pair[0][0]) & (pair[1][1] >= pair[0][1]):
			# count += 1
	print(count)
	
main()