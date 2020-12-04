file = open("input.txt", "r")

lineWidth = 30 # the max position allowed to be accessed in the string array
horizPos = 0 # the position we're at horizontally

treeCount = 0
for line in file:

	if horizPos > lineWidth:
		horizPos -= (lineWidth + 1)
	
	if line[horizPos] == '#':
		treeCount += 1
	
	horizPos += 3
	
print ("There were " + str(treeCount) + " trees.")