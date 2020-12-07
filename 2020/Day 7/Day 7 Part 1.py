import re

with open('input.txt', 'r') as input:
	file = input.readlines()

def findBags(lookFor: set, colors: dict):

	hasMyBag = set(lookFor)
	initialLen = len(hasMyBag)
	
	for key in colors.keys():
		for color in lookFor:
			if color in colors[key]:
				hasMyBag.add(key)

	afterLen = len(hasMyBag)
	if (afterLen - initialLen == 0):
		return hasMyBag
	else:
		return findBags(hasMyBag, colors)


colors = { }
for line in file:
	color = re.findall(r'(.*) bag[s]* contain (.*)', line)

	colorsSupported = set(re.findall(r'\d+ (.*?)? bag[s]*', color[0][1]))
	colors[color[0][0]] = colorsSupported

print(len(findBags(['shiny gold'], colors)))
