def sign(num):
	if num > 0:
		return 1
	elif num < 0:
		return -1
	else:
		return 0


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
	
	directions = {
		"R": (1,0), 
		"L": (-1,0),
		"D": (0,-1),
		"U": (0,1)
		}
	
	instructions = []
	
	for line in lines:
		split = line.split()
		for i in range(int(split[1])):
			instructions.append(directions[split[0]])



	return instructions

def UpdateTail(h,t):

	move = 0,0

	#horizontally aligned, 2+ away: yanked vertically
	if h[0] == t[0] and abs(h[1] - t[1]) > 1:
		moveDir = sign(h[1] - t[1])
		move = 0, moveDir
	
	#vertically aligned, 2+ away: yanked horizontally
	elif h[1] == t[1] and abs(h[0] - t[0]) > 1:
		moveDir = sign(h[0] - t[0])
		move = moveDir, 0

	#aligned on neither axis + not adjacent: tugged diagonally
	elif abs(h[0] - t[0]) + abs(h[1] - t[1]) > 2: #h[0] != t[0] and h[1] != t[1]:
		move = sign(h[0] - t[0]), sign(h[1] - t[1])

	t = [t[0] + move[0], t[1] + move[1]]
	return t


################################################################

puzzleNum = "09"
debug = False

def main():

	instructions = GetData(debug)
	knotCount = 10
	knots = []
	for i in range(knotCount):
		knots.append([0,0])

	visited = []
	visited.append(knots[len(knots) - 1])


	for instruction in instructions:
		
		#move head
		knots[0][0] = knots[0][0] + instruction[0]
		knots[0][1] = knots[0][1] + instruction[1]

		#move each subsequent knot
		for i in range(1,len(knots),1):
			knots[i] = UpdateTail(knots[i-1],knots[i])

		#track the last knot's visit to its new location
		visited.append(knots[len(knots) - 1])
	
	visitedNoDupes = []
	for visit in visited:
		if visitedNoDupes.count(visit) == 0:
			visitedNoDupes.append(visit)
	
	print(len(visitedNoDupes))

main()