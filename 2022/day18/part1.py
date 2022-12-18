from itertools import product
from os.path import dirname
from pprint import pprint
from timeit import repeat


def adjacent(x, y, z):
    for dx, dy, dz in product([-1, 0, 1], repeat=3):
        if sum(map(abs, [dx, dy, dz])) == 1:
            yield x + dx, y + dy, z + dz


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    points = {tuple(map(int, line.split(','))) for line in lines}

    surfaceArea = 0
    for point in points:
        for adjacentPoint in adjacent(*point):
            if adjacentPoint not in points:
                surfaceArea += 1

    print(surfaceArea)


if __name__ == "__main__":
    main()
