import copy

with open('input.txt', 'r') as input:
	rows = list(input.read().split())
	seats = list(map(list, rows))

def checkSurroundings(seats, x, y):

	occupiedCount = 0
	for dX in range(-1, 2):
		for dY in range(-1, 2):
			if 0 > x + dX or x + dX >= len(seats):
				continue
			elif 0 > y + dY or y + dY >= len(seats[x + dX]):
				continue

			if dX == 0 and dY == 0:
				continue
				
			if seats[x + dX][y + dY] == '#':
				occupiedCount += 1

	return occupiedCount

def applyRules(seats):

	newSeats = copy.deepcopy(seats)

	changeCount = 0

	for x in range(len(seats)):
		for y in range(len(seats[x])):

			surroundings = checkSurroundings(seats, x, y)
			if seats[x][y] == 'L' and surroundings == 0:
				newSeats[x][y] = '#' # occupado

			elif seats[x][y] == '#' and surroundings >= 4:
				newSeats[x][y] = 'L' # deoccupado
			else:
				continue

			changeCount += 1 # if reached, neither of the change rules were met
	return (newSeats, changeCount)

seats = (seats, 1)
while True:
	seats = applyRules(seats[0])
	
	if seats[1] == 0:
		break

# count the number of occupado seats
print( sum(seats[0][i].count('#') for i in range(len(seats[0]))))
