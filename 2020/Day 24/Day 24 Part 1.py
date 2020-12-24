import re
## REGEX COMPILATION FOR EFFICIENCY
moves = re.compile(r'(e|se|sw|w|nw|ne)')

def computeTileCoorinates(moves: list) -> tuple:
	"""
	Returns a tuple of the form (x, y) which represents the location of the tile
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

with open('input.txt', 'r') as file:
	lines = file.read().split('\n')

tiles = {} # relates a tuple, (x, y), to a boolean value (True = Black, False = White)
for sequence in lines:
	regex = re.findall(moves, sequence)
	
	coord = computeTileCoorinates(regex)
		
	if coord not in tiles.keys():
		tiles[coord] = True
	else: tiles[coord] = not tiles[coord]

print(sum([tiles[t] for t in tiles.keys() if tiles[t]]))