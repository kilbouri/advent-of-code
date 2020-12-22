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
			return (target, nums[0 : i])

def setFind(nums: list, expectedSum: int):

	print(f"Finding a contiguous set that sums to {expectedSum}...")

	for start in range(0, len(nums)):
		for end in range(len(nums), start, -1):

			sliced = nums[start : end]
			if sum(sliced) == expectedSum:
				minNum = min(sliced)
				maxNum = max(sliced)

				print("Match: " + str(sliced))
				print(f"Code: {minNum + maxNum}")
				return


res = find(25)
setFind(list(res[1]), res[0])