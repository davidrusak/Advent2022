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

class Dir():
	def __init__(self, name, parent):
		self.name = name
		self.files = []
		self.subdirs = {}
		self.parent:Dir = parent

def BuildFileStructure(data:list):
	topDir = Dir("", None)
	topDir.subdirs["/"] = Dir("/",topDir)
	currentDir = topDir

	for line in data:
		# print("line")
		splitLine = line.split()


		#    "$" - instruction
		if line[0] == "$":

			#navigation instruction
			if splitLine[1] == "cd":
				
				#go up one
				if splitLine[2] == "..":
					currentDir = currentDir.parent
				
				#go down into a subdir
				else:
					currentDir = currentDir.subdirs[splitLine[2]]
			elif splitLine[1] == "ls":
				#don't really have to do anything
				continue
			else :
				print("Wtf")
				
		#    number - file in current dir
		elif line[0].isnumeric():
			currentDir.files.append(int(splitLine[0]))

		#    letter - subdir in current dir
		elif splitLine[0] == "dir":
			currentDir.subdirs[splitLine[1]] = Dir(splitLine[1],currentDir)
		
		else:
			print("Wtf")

	return topDir

def GetDirSize(dir:Dir):
	sum = 0
	for file in dir.files:
		sum += file
	for subdir in dir.subdirs:
		sum += GetDirSize(dir.subdirs[subdir])
	
	print("Size of dir " + dir.name + ": " + str(sum))
	dirsizes.append(sum)
	
	return sum

################################################################

puzzleNum = "07"
debug = False

dirsizes = []

def main():
	
	data = GetData(debug)

	topDir = BuildFileStructure(data)

	GetDirSize(topDir.subdirs["/"])

	#6.1
	sizes = [size for size in dirsizes if size < 100000]
	print(sizes)
	sizeSum = 0
	for size in sizes: sizeSum += size
	print("final sum: " + str(sizeSum))

	#6.2

	print("6.2: ")
	totalSpace = 70000000
	neededSpace = 30000000
	
	usedSpaceSum = GetDirSize(topDir)
	maxUsed = totalSpace - neededSpace
	needToFree = usedSpaceSum - maxUsed
	print("can use no more than " + str(maxUsed) + ", so need to free " + str(needToFree))
	
	leastSufficientDirToKill = usedSpaceSum
	for size in dirsizes: 
		if (size < leastSufficientDirToKill) & (size >= needToFree):
			leastSufficientDirToKill = size

	print(leastSufficientDirToKill)

main()