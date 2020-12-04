input = (138241, 674034) # range of values the password can be in

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits either increase or stay the same

def checkPassword(password: int):
		foundRepeat = False
		lastNumber = 0
		for num in str(password):

			# is this digit greater than the previous?
			if int(num) > lastNumber:
				lastNumber = int(num)
				continue

			# have we found the first repeat?
			elif int(num) == lastNumber:
				foundRepeat = True
				continue

			# if number is less or equal to previous and already found repeat,
			# the password is invalid
			elif int(num) < lastNumber:
				return False

		return foundRepeat

min, max = input
validCount = 0
print ("Thinking...")
for password in range(min, max + 1):
	if checkPassword(password) is True:
		validCount += 1

print("There were " + str(validCount) + " valid passcodes in the range.")