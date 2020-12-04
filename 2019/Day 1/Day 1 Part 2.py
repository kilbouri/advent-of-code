fuelTotal = 0

with open('input.txt', 'r') as input:
	for mass in input:
		fuel = int(mass) // 3 - 2
		newFuel = int(mass) // 3 - 2
		while (newFuel > 0):
			fuelTotal += newFuel
			newFuel = newFuel // 3 - 2

print(fuelTotal)