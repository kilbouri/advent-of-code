from os import getcwd
import re
import copy


def adjacentCoordinates(x, y):
    yield (x+1,  y)  # E
    yield (x-1,  y)  # W
    yield (x+.5, y-.5)  # SE
    yield (x-.5, y-.5)  # SW
    yield (x+.5, y+.5)  # NE
    yield (x-.5, y+.5)  # NW


def computeTileCoorinates(moves: list) -> tuple:
    x = 0
    y = 0

    for move in moves:
        if move == "e":
            x += 1
        elif move == "se":
            x += 0.5
            y -= 0.5
        elif move == "sw":
            x -= 0.5
            y -= 0.5
        elif move == "w":
            x -= 1
        elif move == "ne":
            x += 0.5
            y += 0.5
        elif move == "nw":
            x -= 0.5
            y += 0.5

    return (x, y)


def countAdjacentTiles(x, y, others: dict):
    ot = [others.get(a, False) for a in adjacentCoordinates(x, y)]
    blackTiles = sum(ot)
    whiteTiles = 6 - blackTiles

    return (whiteTiles, blackTiles)


def doDay(t: dict) -> dict:
    visited = set()
    newTiles = copy.deepcopy(t)
    for (u, v) in t.keys():
        toVisit = list(adjacentCoordinates(u, v)) + [(u, v)]
        for tile in toVisit:
            if tile in visited:
                continue

            visited.add(tile)

            # visits the adjacent tiles
            _, ab = countAdjacentTiles(tile[0], tile[1], t)

            if t.get(tile, False) and (ab == 0 or ab > 2):
                newTiles[tile] = False

            elif (not t.get(tile, False)) and ab == 2:
                newTiles[tile] = True

    return newTiles


def main():
    moves = re.compile(r"(e|se|sw|w|nw|ne)")

    with open(f"{getcwd()}/2020/day24/input.txt", "r") as file:
        lines = file.read().split("\n")

    # relates a tuple, (x, y), to a boolean value (True = Black, False = White)
    tiles = {}
    for sequence in lines:
        regex = re.findall(moves, sequence)
        coord = computeTileCoorinates(regex)

        tiles[coord] = not tiles.get(coord, False)

    for i in range(100):
        print(f"Now simulating day {i + 1}")
        tiles = doDay(tiles)

    print(sum(tiles.values()))


if __name__ == "__main__":
    main()
