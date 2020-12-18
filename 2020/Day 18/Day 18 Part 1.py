import re
with open('input.txt', 'r') as file:
	expressions = file.read().split("\n")

def indexReplace(source: str, replaceWith: str, start: int, end: int) -> str:
	"""
	Utility function for replacing at indices within a string.

	Parameters:
	source - the string to replace the substring in
	replaceWith - the new substring
	start - the starting index
	end - the ending index
	"""
	return str(source)[:start] + str(replaceWith) + str(source)[end:]

def findBrackets(expr: str) -> tuple:
	"""
	Returns a tuple of the form ((start, end), string) where start and end
	are the indices of the substring which contains string. Trims the brackets.
	Returns None if no brackets are found.

	Parameters:
	expr - the expression to look for brackets in
	"""
	regex = re.search(r'\(([\d \*\+]*)\)', str(expr))

	if regex is None:
		return None
	else:
		start = regex.span()[0]
		end = regex.span()[1]
		match = regex.group()[1:-1]

		return ((start, end), match)

def findOperation(expr: str) -> tuple:
	"""
	Returns a tuple of the form ((start, end), operand, operation, operand) where
	the tuple (start, end) contains the first and last indices of the matching
	substring.
	Returns None if no operation is found.

	Parameters:
	expr - the expression to look for operations in
	"""
	regex = re.search(r'\(*(\d+) (\*|\+) (\d+)\)*', str(expr))

	if not regex:
		return None
	else:
		start = regex.span()[0]
		end = regex.span()[1]
		operandA = regex.groups()[0]
		operation = regex.groups()[1]
		operandB = regex.groups()[2]

		return ((start, end), operandA, operation, operandB)

def evaluateExpression(expr: str):

	newExpression = expr
	brackets = findBrackets(expr)
	if brackets:
		indices = brackets[0]
		newSubstring = evaluateExpression(brackets[1])
		
		newExpression = indexReplace(newExpression, newSubstring, indices[0], indices[1])
		return evaluateExpression(newExpression)
	else:
		operation = findOperation(expr)
		if operation:
			indices = operation[0]

			operandA = int(operation[1])
			operandB = int(operation[3])

			newSubstring = ""

			if operation[2] == '+':
				newSubstring = str(operandA + operandB)
			elif operation[2] == '*':
				newSubstring = str(operandA * operandB)

			newExpression = indexReplace(newExpression, newSubstring, indices[0], indices[1])
			return evaluateExpression(newExpression)

		else:
			return int(expr)

total = 0
for expression in expressions:
	result = evaluateExpression(expression)
	total += result

print("Total: " + str(total))