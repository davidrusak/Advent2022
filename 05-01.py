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

	breakLine = -1

	#find the break btwn the stacks & instructions
	for i in range(len(lines)):
		if lines[i] == "":
			breakLine = i
			break

	#process the stacks
	stacksLines = lines[:breakLine]

	#the numbers at the bottom of the stacks:
	stackTitles = stacksLines[len(stacksLines)-1]

	#find what char index those numbers are at and then collect all letters found above them:
	stacks = []
	for i in range (len(stackTitles)):
		if stackTitles[i] != " ":
			thisStack = []
			for j in range(len(stacksLines)-1):
				if stacksLines[j][i] != " ":
					thisStack.append(stacksLines[j][i])
			stacks.append(thisStack)



	#process the instructions
	instructionsLines = lines[breakLine + 1:]
	instructions = []
	for instr in instructionsLines:
		split = instr.split()

		#count, from, to
		instructions.append([int(split[1]),int(split[3]),int(split[5])])

	return stacks, instructions


def FollowInstruction(stacks, instr):
	#instr: count, from, to
	count = instr[0]
	frum = instr[1] - 1
	to = instr[2] - 1

	for i in range(count):
		moved = stacks[frum].pop(0)
		stacks[to].insert(0,moved)

def FollowInstruction9001(stacks, instr):
	#instr: count, from, to
	count = instr[0]
	frum = instr[1] - 1
	to = instr[2] - 1

	for i in range(count - 1, -1, -1):
		moved = stacks[frum].pop(i)
		stacks[to].insert(0,moved)
		
		

################################################################

puzzleNum = "05"
debug = False


def main():
	stacks, instructions = GetData(debug)

	for instr in instructions:
		FollowInstruction9001(stacks, instr)

	result = ""
	for stack in stacks:
		result += stack[0]
	print(result)
	
	
main()