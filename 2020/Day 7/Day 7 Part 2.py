import re

with open('input.txt', 'r') as input:
	file = input.readlines()


colorCount = { }
for line in file:
	color = re.findall(r'(.*) bag[s]* contain (.*)', line)

	regexResult = re.findall(r'(?:(\d+) (.*?)? bag[s]*)|(no other bags)', color[0][1])

	counts = list()
	for quant in regexResult:
		if quant[0] == '' and quant[1] == '':
			countAndColor = (0, '')
			counts.append(countAndColor)
		else:
			countAndColor = (quant[0], quant[1])
			counts.append(countAndColor)
	
	colorCount[color[0][0]] = counts

# we now have a dictionary of the count of each color of bag within each bag
# time to do some nasty shit to find the number of bags starting from 'shiny gold'
def countNestedBags(color: str, nestQuants: dict):
	if (nestQuants[color])[0][0] == 0:
		return 0

	else:
		nestCount = 0
		for bag in nestQuants[color]:
			addedBags = int(bag[0]) * (countNestedBags(bag[1], nestQuants) + 1)
			nestCount += addedBags
		return nestCount

print (countNestedBags('shiny gold', colorCount))