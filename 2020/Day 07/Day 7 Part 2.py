import re

with open('input.txt', 'r') as input:
	file = input.readlines()

colorCount = { }
for line in file:
	color = re.findall(r'(.*) bag[s]* contain (.*)', line)

	nestedBags = re.findall(r'(?:(\d+) (.*?)? bag[s]*)|(no other bags)', color[0][1])

	counts = list()
	for bag in nestedBags:
		if not bag[0] or not bag[1]:
			countAndColor = (0, '')
			counts.append(countAndColor)
		else:
			countAndColor = (bag[0], bag[1])
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
