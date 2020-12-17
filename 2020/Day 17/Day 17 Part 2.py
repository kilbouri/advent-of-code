import copy

with open('input.txt', 'r') as file:
	file = file.read()

# Z slice - the up/down in the pocket dimension
# Y slice - the up/down in each Z slice printed to the screen
# X slice - the left/right in each Z slice printed to the screen

cubeCorner1 = [-10, -10, -10, -10]
cubeCorner2 = [10, 10, 10, 10]

def getCube(pocket: dict, x: int, y: int, z: int, w: int) -> bool:
	return pocket[w][z][y][x] == '#'

def shouldBeActive(pocket: dict, x: int, y: int, z: int, w: int) -> bool:
	cubeState = getCube(pocket, x, y, z, w)

	adjacentActive = 0
	adjacentInactive = 0

	for dx in range(-1, 2):
		for dy in range(-1, 2):
			for dz in range(-1, 2):
				for dw in range(-1, 2):
					if dx == 0 and dy == 0 and dz == 0 and dw == 0:
						continue
					
					if getCube(pocket, x + dx, y + dy, z + dz, w + dw):
						adjacentActive += 1
					else:
						adjacentInactive += 1

	if cubeState:
		if adjacentActive == 2 or adjacentActive == 3:
			return True
	else:
		if adjacentActive == 3:
			return True
	
	return False

def simCycle(pocket: dict):
	newPocket = copy.deepcopy(pocket)

	for w in range(cubeCorner1[0] + 1, cubeCorner2[0]):
		for z in range(cubeCorner1[1] + 1, cubeCorner2[1]):
			for y in range(cubeCorner1[2] + 1, cubeCorner2[2]):
				for x in range(cubeCorner1[3] + 1, cubeCorner2[3]):
					sba = shouldBeActive(pocket, x, y, z, w)
					if sba:
						newPocket[w][z][y][x] = '#'
					else:
						newPocket[w][z][y][x] = '.'

	return newPocket


def countActive(pocket: dict):
	active = 0
	for w in range(cubeCorner1[0], cubeCorner2[0] + 1):
		for z in range(cubeCorner1[1], cubeCorner2[1] + 1):
			for y in range(cubeCorner1[2], cubeCorner2[2] + 1):
				for x in range(cubeCorner1[3], cubeCorner2[3] + 1):
					if getCube(pocket, x, y, z, w):
						active += 1
					
	return active

pocketDimension = {}
for w in range(cubeCorner1[0], cubeCorner2[0] + 1):
	pocketDimension[w] = {}
	for z in range(cubeCorner1[1], cubeCorner2[1] + 1):
		pocketDimension[w][z] = {}
		for y in range(cubeCorner1[2], cubeCorner2[2] + 1):
			pocketDimension[w][z][y] = {}
			for x in range(cubeCorner1[3], cubeCorner2[3] + 1):
				pocketDimension[w][z][y][x] = '.'
 
ySlices = file.split('\n')
ySlice = {}
for y, xSlice in enumerate(ySlices):
	for x, cube in enumerate(xSlice):
		pocketDimension[0][0][y-4][x-4] = cube

for i in range(0, 6):
	print(f"Running cycle {i}...")
	pocketDimension = simCycle(pocketDimension)

print("Counting...")
print(countActive(pocketDimension))