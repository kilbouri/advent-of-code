def countTrees(right: int, down: int):
	lineWidth = 30 # the max position allowed to be accessed in the string array

	horizPos = 0 # the position we're at horizontally
	treeCount = 0
	
	_down = down
	with open("input.txt", "r") as file:
	
		for line in file:
			if _down != down:
				_down += 1
				continue
			else:
				_down = 1
		
			if horizPos > lineWidth:
				horizPos -= lineWidth+1

			if line[horizPos] == '#':
				treeCount += 1

			horizPos += right

	return treeCount

print("We will encounter " + 
	str(int(countTrees(1, 1)) * 
	    int(countTrees(3, 1)) *
		int(countTrees(5, 1)) * 
		int(countTrees(7, 1)) * 
		int(countTrees(1, 2)))
	+ " trees.")