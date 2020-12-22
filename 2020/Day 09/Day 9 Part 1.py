with open("input.txt", 'r') as file:
	nums = list(map(int, file.read().split()))

def find(ambLen: int):
	for i in range(ambLen, len(nums)):
		
		target = nums[i]
		sliced = set(nums[i - (ambLen) : i])

		found = False
		for first in sliced:
			
			second = target - first
			
			if second in sliced and first != second:
				found = True
				break

			else:
				continue
		
		if not found:
			print("Did not have a match: " + str(target))
			return

find(25)