import re

with open('input.txt', 'r') as input:
	file = input.read()

def tryBootCode(bootCode: list):
	cpuCounter = 0
	accumulator = 0
	addressesVisted = list()
	while cpuCounter < len(bootCode):

		op = bootCode[cpuCounter]

		if cpuCounter in addressesVisted:
			return False

		addressesVisted.append(cpuCounter)

		if op[0] == 'jmp':
			cpuCounter += int(op[1])
			continue
		elif op[0] == 'acc':
			accumulator += int(op[1])

		cpuCounter += 1
	if (cpuCounter == len(bootCode)):
		return accumulator
	else:
		return False

def __main__():
	operations = re.findall(r'(nop|jmp|acc) (\+\d+|-\d+)', file)
	for i in range(0, len(operations)):
		opMutation = operations.copy()

		if operations[i][0] == 'nop':
			opMutation[i] = ('jmp', operations[i][1])
			worked = tryBootCode(opMutation)

			if worked is not False:
				print(worked)
				return

			else:
				opMutation = operations.copy()

		elif operations[i][0] == 'jmp':
			opMutation[i] = ('nop', operations[i][1])
			worked = tryBootCode(opMutation)
			
			if worked is not False:
				print(worked)
				return
			else:
				opMutation = operations.copy()

__main__()