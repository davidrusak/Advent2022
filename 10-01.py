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
		
	instructions = []
	for line in lines:
		split = line.split()
		if split[0] == "addx":
			split[1] = int(split[1])
		instructions.append(split)


	return instructions

def ProcessInstruction(instruction, X, curCycle):

	cycleCount = 0
	incrementAmt = 0

	global printout

	if instruction[0] == "noop":
		cycleCount = 1
	else:
		cycleCount = 2
		incrementAmt = instruction[1]

	#increment the cycle as many times as you should, logging X if needed
	newCycle = curCycle
	for cycle in range(cycleCount):
		#draw this cycle's dots
		curPos = (newCycle - 1) % 40
		if abs(curPos - X) < 2:
			printout += "#"
		else:
			printout += "."


		if checkTimes.count(newCycle) > 0:
			# print("we're on the check cycle!" + str(newCycle))
			checkXValues.append(X * newCycle)
		
		if newCycle % 40 == 0:
			printout += "\n"
		newCycle += 1

	#perform the operation
	newX = X + incrementAmt
	return newX, newCycle

	
	
		




################################################################

puzzleNum = "10"
debug = False
checkTimes = [20,60,100,140,180,220]
checkXValues = []
printout = ""

def main():

	cycleCount = 220
	X = 1
	curCycle = 1

	instructions = GetData(debug)
	for instruction in instructions:
		X, curCycle = ProcessInstruction(instruction, X, curCycle)


	print(checkXValues)
	sum = 0
	for val in checkXValues:
		sum+=val
	print(sum)

	print(printout)

main()