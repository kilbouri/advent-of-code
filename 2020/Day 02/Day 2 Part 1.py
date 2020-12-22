import re

file = open("input.txt", "r")

validCount = 0
for line in file:
	
	stuffs = re.findall(r'(\d+)-(\d+) (.): (.*)', line) 
	res = list(stuffs)
	
	min, max, character, password = res[0]
	occurences = password.count(character)
	
	if (occurences in range(int(min), int(max) + 1)):
		validCount += 1
		
print ("There were " + str(validCount) + " valid passwords in the DB")