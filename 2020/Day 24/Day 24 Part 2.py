import re
import copy
## REGEX COMPILATION FOR EFFICIENCY
moves = re.compile(r'(e|se|sw|w|nw|ne)')

def adjacentCoordinates(x, y):
	yield (x+1,  y) # E
	yield (x-1,  y) # W
	yield (x+.5, y-.5) # SE
	yield (x-.5, y-.5) # SW
	yield (x+.5, y+.5) # NE
	yield (x-.5, y+.5) # NW

def computeTileCoorinates(moves: list) -> tuple:
	"""
	Returns a tuple of the form (x, y) which represents the location of the tile

	Parameters:
	moves - the list of moves taken from the reference point to get to the tile
	"""
	x = 0
	y = 0

	for move in moves:
		if move == 'e':
			x += 1
		elif move == 'se':
			x += 0.5
			y -= 0.5
		elif move == 'sw':
			x -= 0.5
			y -= 0.5
		elif move == 'w':
			x -= 1
		elif move == 'ne':
			x += 0.5
			y += 0.5
		elif move == 'nw':
			x -= 0.5
			y += 0.5

	return (x, y)

def countAdjacentTiles(x, y, others: dict):
	"""
	Returns a tuple of the form (white, black). If an adjacent tile isn't
	in the dictionary, then it is assumed to be in the starting position (white)

	Parameters:
	x, y - the tuple coordinates of the tile to check
	others - the dictionary of other tiles
	"""
	ot = [others.get(a, False) for a in adjacentCoordinates(x, y)]
	blackTiles = sum(ot)
	whiteTiles = 6 - blackTiles

	return (whiteTiles, blackTiles)

def doDay(ts: dict) -> dict:
	"""
	Returns a new dictionary with the next day's changed tiles

	Parameters:
	t - the dictionary of all tiles
	"""
	visited = set()
	newTiles = copy.deepcopy(ts)
	for (u, v) in ts.keys():
		toVisit = list(adjacentCoordinates(u, v)) + [(u, v)]
		for tile in toVisit:
			if tile in visited:
				continue

			visited.add(tile)

			_, ab = countAdjacentTiles(tile[0], tile[1], tiles) # visits the adjacent tiles

			if ts.get(tile, False) and (ab == 0 or ab > 2):
				newTiles[tile] = False

			elif (not ts.get(tile, False)) and ab == 2:
				newTiles[tile] = True

	return newTiles

with open('input.txt', 'r') as file:
	lines = file.read().split('\n')

tiles = {} # relates a tuple, (x, y), to a boolean value (True = Black, False = White)
for sequence in lines:
	regex = re.findall(moves, sequence)
	coord = computeTileCoorinates(regex)

	tiles[coord] = not tiles.get(coord, False)

for _ in range(100):
	tiles = doDay(tiles)
	
print(sum(tiles.values()))