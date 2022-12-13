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
	
	monkeys = []
	for i in range(0, len(lines), 7):

		itemsLine = lines[i+1][18:].split(", ")
		items = []
		for item in itemsLine:
			items.append(int(item))

		operation = lines[i+2][23:24]
		operationObj = lines[i+2][25:]
		divisor = int(lines[i+3][21:])
		trueThrowTarget = int(lines[i+4][29:])
		falseThrowTarget = int(lines[i+5][30:])

		monkeys.append(Monkey(items,operation,operationObj,divisor,trueThrowTarget,falseThrowTarget))
		
	return monkeys

class Monkey():
	def __init__(self, items, operation, operationObj, divisor, trueThrowTarget, falseThrowTarget):
		self.items = items
		self.operation = operation
		self.operationObj = operationObj
		self.divisor = divisor
		self.trueThrowTarget = trueThrowTarget
		self.falseThrowTarget = falseThrowTarget
		self.inspectCount = 0
		
def ProcessWorry(old, operation, operationObj):
	obj = -1
	if operationObj.isnumeric():
		obj = int(operationObj)
	else:
		obj = old


	if operation == "+":
		return old + obj
	elif operation == "*":
		return old * obj
	else:
		print("WTF")
		return -1

def ProcessMonkey(index, monkeys):
	global lcm
	monkey:Monkey = monkeys[index]
	for i in range(len(monkey.items)):

		#you'll always throw the first one
		itemIndex = 0
		#do the specified worry operation
		monkey.items[itemIndex] = ProcessWorry(monkey.items[itemIndex],monkey.operation,monkey.operationObj)
		#divide it by 3
		# monkey.items[itemIndex] = monkey.items[itemIndex] // 3
		
		#lcm it
		monkey.items[itemIndex] = monkey.items[itemIndex] % lcm

		#determine the monkey this is thrown to
		throwTarg = -1
		if monkey.items[itemIndex] % monkey.divisor == 0:
			throwTarg = monkey.trueThrowTarget
		else:
			throwTarg = monkey.falseThrowTarget
		
		#throw
		thrown = monkey.items.pop(itemIndex)
		monkeys[throwTarg].items.append(thrown)

		#increment inspectCount
		monkey.inspectCount = monkey.inspectCount + 1

def GetInspectCount (monkey):
	return monkey.inspectCount

################################################################

puzzleNum = "11"
debug = False
lcm = 0

def main():
	global lcm
	monkeys = GetData(debug)

	for monkey in monkeys:
		if lcm == 0:
			lcm = monkey.divisor
		else:
			lcm *= monkey.divisor
	print (lcm)

	roundCount = 10000
	for round in range (roundCount):
		for monkeyIndex in range(len(monkeys)):
			ProcessMonkey(monkeyIndex, monkeys)

	monkeys.sort(reverse=True, key=GetInspectCount)

	print(monkeys[0].inspectCount * monkeys[1].inspectCount)

main()