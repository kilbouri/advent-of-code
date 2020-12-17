import re

def validateTicket(ticket: list, attrRanges: dict) -> bool:
	"""
	Returns true of the each of the provided ticket's numbers can be
	found in at least one of the ranges in the attributes provided

	Parameters:
	ticket - the list of integers representing the ticket
	attrRanges - a dictionary providing a group of ranges for each attribute
	"""
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

def strToTicket(tickStr: str) -> list:
	"""
	Returns a list of integers representing the numbers in this ticket.

	Parameters:
	tickStr - the string representing the ticket, in the format '\d+, \d+....'
	"""
	return list(map(int, tickStr.split(',')))

def checkFieldSet(validTickets: list, fieldSet: list, attrRanges: dict) -> bool:
	"""
	Returns true of the provided set of fields (in order of index)
	matches all valid tickets provided.

	Parameters:
	validTickets - the tickets that are valid
	fieldSet - the combination of keys in order of index
	attrRanges - the dictionary for looking up valid ranges for each attribute
	"""
	for ticket in validTickets:
		for i, field in enumerate(fieldSet):
			validNumber = False
			for rng in attrRanges[field]:
				if ticket[i] in rng:
					validNumber = True
					break
			if not validNumber: 
				return False
	return True

def generateArrangement(ticket: list, attrRanges: dict) -> list:
	"""
	Returns a list of sets of possible fields for each index in the ticket

	Parameters:
	ticket - the ticket to generate for
	attrRanges - a dictionary to look up the valid ranges for numbers for fields
	"""

	result = []
	for number in ticket:
		validAttributes = set()
		for key in attrRanges.keys():
			for rng in attrRanges[key]:
				if number in rng:
					validAttributes.add(key)

		result.append(validAttributes)
	
	return result
	
with open('input.txt', 'r') as file:
	file = file.read().split("\n\n")

# file indices: 0-ticket pattern   1-your ticket   2-other tickets
regRes = re.findall(r'(.*): (\d+-\d+) or (\d+-\d+)', file[0])

# contains a string name, and a list of valid ranges
intToAttrName = {}
attributes = {}
for index, result in enumerate(regRes):
	intToAttrName[index] = result[0]
	ranges = []
	for i in range(1, len(result)):
		spl = result[i].split("-")
		ranges.append(range(int(spl[0]), int(spl[1]) + 1))
	attributes[index] = ranges
	
allOtherTickets = list(strToTicket(t) for t in (file[2].split('\n'))[1:])
validTickets = list(filter(lambda ticket: validateTicket(ticket, attributes), allOtherTickets))

# generate the possible fields for each ticket
possibleFields = {} # contains a list of sets for each index
for ticket in validTickets:
	result = generateArrangement(ticket, attributes)
	for index, fSet in enumerate(result):
		# We use set intersection here to reduce pointless checks later on.
		# Since all tickets must have the same layout of fields, if a given
		# ticket has a new field (except, of course, the first one generated)
		# then it's unique to some subset of the valid tickets and therefore
		# not a valid field label.
		if index in possibleFields.keys():
			possibleFields[index] &= fSet
		else:
			possibleFields[index] = fSet

print("Removing guaranteed fields...")
removed = True
while removed:
	removed = False
	for key in possibleFields.keys():
		if len(possibleFields[key]) == 1:
			known = list(possibleFields[key])[0]
			for subkey in possibleFields.keys():
				if subkey == key:
					continue
				elif known in possibleFields[subkey]:
					newVal = possibleFields[subkey]
					newVal.remove(known)
					possibleFields[subkey] = newVal
					removed = True

print("Generating arrangements...")
possibleArrangements = list(possibleFields[0])
for i in range(1, len(possibleFields.keys())):
	newPossibleArrangements = list()

	for arrangement in possibleArrangements:
		for field in possibleFields[i]:
			if type(arrangement) == int:
				arrangement = [arrangement]
			
			arrangement.append(field)
			newPossibleArrangements.append(arrangement)
	if newPossibleArrangements:
		possibleArrangements = newPossibleArrangements

print(f"Created {len(possibleArrangements)} arrangements.")
print()
matches = list(filter(lambda arrangement: checkFieldSet(validTickets, arrangement, attributes), possibleArrangements))

print("Stringifying the first matching layout...")
stringified = []
for i in matches[0]:
	stringified.append(intToAttrName[i])

myTicket = list(map(int, file[1].split("\n")[1].split(',')))

product = 1
for i, field in enumerate(stringified):
	if "departure" in field:
		product *= myTicket[i]

print(product)