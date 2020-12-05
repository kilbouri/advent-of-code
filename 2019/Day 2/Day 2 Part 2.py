def compute(memory):
	i = 0
	while i < len(memory):
		opcode = int(memory[i])

		if (opcode == 99):
			break
		elif (opcode == 1):
			pos1 = int(memory[i + 1])
			pos2 = int(memory[i + 2])
			pos3 = int(memory[i + 3])
			sum  = int(memory[pos1]) + int(memory[pos2])
			memory[pos3] = str(sum)
		elif (opcode == 2):
			pos1 = int(memory[i + 1])
			pos2 = int(memory[i + 2])
			pos3 = int(memory[i + 3])
			product = int(memory[pos1]) * int(memory[pos2])
			memory[pos3] = str(product)

		i += 4
	return int(memory[0])

def __main__(maxrange: int):
	with open('input.txt', 'r') as input:
		factoryMemory = input.read().split(',')

	operand1: int = range(maxrange)
	operand2: int = range(maxrange)
	result = 0

	for i in operand1:
		for j in operand2:
			# prepare the new memory 
			instructions = factoryMemory.copy()
			instructions[1] = i
			instructions[2] = j

			try:
				print("Trying Noun: " + str(i) + ", Verb: " + str(j))
				result = compute(instructions)
			except IndexError:
				continue # some parameters may modify things that cause errors
			
			if (result == 19690720):
				print("Noun: " + str(i) + ", Verb: " + str(j) + ", Result: " + str(100 * i + j))
				return

__main__(75)