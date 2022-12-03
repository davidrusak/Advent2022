def GetData(debug):
	
	if debug == True:
		file = open("01-testdata.txt","r")
	else:
		file = open("01-data.txt","r")
	lines = file.readlines()
	
	#sanitize all the /ns out
	for i in range(len(lines)):
		lineBreakIndex = lines[i].find("\n")
		if lineBreakIndex >= 0:
			lines[i] = lines[i][:lineBreakIndex]

	#assemble the elves
	elves = []
	thisElf = 0
	for y in range(len(lines)):
		line = lines[y]
		if line == "":
			elves.append(thisElf)
			thisElf = 0
		else:
			thisElf += int(line)
	elves.append(thisElf)
	
	return elves

def GetHighestCalorieCount(elves) :

	highest = 0

	for i in range (len(elves)):
		if elves[i] > highest:
			highest = elves[i]
	return highest

def GetHighestThreeCalorieCounts(elves) :

	highest = [0,0,0]

	for i in range (len(elves)):

		elf = elves[i]

		#cycle back through the array and slot it in then bump off the bottom item
		for j in range(len(highest)-1, -1, -1):
			if elf > highest[j]:
				if j == 0:
					highest.insert(0,elf)
					highest = highest[:len(highest)-1]
				elif elf <= highest[j-1]:
					highest.insert(j,elf)
					highest = highest[:len(highest)-1]
				


	return highest

def SumArray(array) :
	sum = 0
	for i in range(len(array)):
		sum += array[i]
	return sum



################################################################

debug = False

def main():
	elves = GetData(debug)
	print("There are this many elves: " + str(len(elves)))
	#print("highest calories: " + str(GetHighestCalorieCount(elves)))
	threeHighest = GetHighestThreeCalorieCounts(elves)
	print("three highest total:")
	print(SumArray(threeHighest))
	
	
main()