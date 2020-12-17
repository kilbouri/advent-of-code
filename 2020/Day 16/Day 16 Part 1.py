import re

with open('input.txt', 'r') as file:
	file = file.read().split("\n\n")

# file indices: 0-ticket pattern   1-your ticket   2-other tickets
regRes = re.findall(r'(.*): (\d+-\d+) or (\d+-\d+)', file[0])

# contains a string name, and a tuple of the valid ranges
attributes = {}
for result in regRes:
	ranges = []
	for i in range(1, len(result)):
		spl = result[i].split("-")
		ranges.append(range(int(spl[0]), int(spl[1]) + 1))
	attributes[result[0]] = ranges

def validateTicket(ticket: list, attrRanges: dict) -> any:
	for number in ticket:
		validNumber = False
		for key in attrRanges.keys():
			for rng in attrRanges[key]:
				if number in rng:
					validNumber = True
					break
			if validNumber:
				break
				
		if not validNumber:
			return False
	return True

def strToTicket(tickStr: str):
	return list(map(int, tickStr.split(',')))

allOtherTickets = list(strToTicket(t) for t in (file[2].split('\n'))[1:])

errorSum = 0
for ticket in allOtherTickets:
	validTicket = True
	for num in ticket:
		validNum = False
		for key in attributes.keys():
			ranges = attributes[key]
			for rng in ranges:
				if num in rng:
					validNum = True
					break
			if validNum:
				break

		if not validNum:
			validTicket = False
			errorSum += num
			break
print(errorSum)