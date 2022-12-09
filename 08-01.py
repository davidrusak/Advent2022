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
	
	trees = []
	seens = []
	scenics = []
	for row in lines:
		thisTreeRow = []
		thisSeenRow = []
		thisScenicRow = []
		for chr in row:
			thisTreeRow.append(int(chr))
			thisSeenRow.append(False)
			thisScenicRow.append(0)
		trees.append(thisTreeRow)
		seens.append(thisSeenRow)
		scenics.append(thisScenicRow)

	return trees, seens, scenics

def DoFirstPuzzle(trees, seens) :
	for y in range(len(trees)):
		row = trees[y]
		curHeight = -1
		for xFwd in range(len(row)):
			if row[xFwd] > curHeight:
				seens[y][xFwd] = True
				curHeight = row[xFwd]
			# else:
			# 	break

		curHeight = -1
		for xBwd in range(len(row) -1, -1, -1):
			if row[xBwd] > curHeight:
				seens[y][xBwd] = True
				curHeight = row[xBwd]
			# else:
			# 	break
	
	for x in range(len(trees[0])):
		curHeight = -1
		for yFwd in range(len(trees)):
			if trees[yFwd][x] > curHeight:
				seens[yFwd][x] = True
				curHeight = trees[yFwd][x]
		
		curHeight = -1
		for yBwd in range(len(trees) - 1, -1, -1):
			if trees[yBwd][x] > curHeight:
				seens[yBwd][x] = True
				curHeight = trees[yBwd][x]

	sum = 0
	for row in seens:
		for seen in row:
			if seen == True: 
				sum += 1

	print("8.1 count of seen trees:")
	print(sum)

def DoSecondPuzzle (trees, scenics) :

	highestScenic = 0

	for y in range(len(trees)):
		for x in range(len(trees[y])):
			scenic = GetScenicScore(y,x,trees)
			scenics[y][x] = scenic
			highestScenic = max(highestScenic, scenic)

	print("8.2 highest scenic score: ")
	print(highestScenic)
			

def GetScenicScore(yPos,xPos,trees):

	if yPos == 3 and xPos == 2:
		print("this one")

	height = trees[yPos][xPos]

	xFwdScore = len(trees[yPos]) - 1 - xPos
	for xFwd in range(xPos + 1,len(trees[yPos]),1):
		if trees[yPos][xFwd] >= height:
			xFwdScore = xFwd - xPos
			break


	xBwdScore = xPos
	for xBwd in range(xPos -1,-1,-1):
		if trees[yPos][xBwd] >= height:
			xBwdScore = xPos - xBwd
			break
	
	yFwdScore = len(trees) - 1 - yPos
	for yFwd in range(yPos + 1, len(trees),1):
		if trees[yFwd][xPos] >= height:
			yFwdScore = yFwd - yPos
			break

	yBwdScore = yPos
	for yBwd in range(yPos -1, -1, -1):
		if trees[yBwd][xPos] >= height:
			yBwdScore = yPos - yBwd
			break

	return xFwdScore * xBwdScore * yFwdScore * yBwdScore


################################################################

puzzleNum = "08"
debug = False

dirsizes = []

def main():

	trees, seens, scenics = GetData(debug)

	#8.1
	DoFirstPuzzle(trees, seens)

	#8.2
	DoSecondPuzzle(trees, scenics)

main()