from os.path import dirname
from pprint import pprint as print

from itertools import product


def visible(grid: list[list[int]], x: int, y: int):
    rows, cols = len(grid), len(grid[0])

    # outer edges are visible cuz there are no trees before them
    if x in [0, cols - 1] or y in [0, rows - 1]:
        return True

    # allows nice concise logic below
    gridTranspose = list(zip(*grid))

    return grid[y][x] > max(gridTranspose[x][0:y]) \
        or grid[y][x] > max(gridTranspose[x][y+1:rows]) \
        or grid[y][x] > max(grid[y][0:x]) \
        or grid[y][x] > max(grid[y][x+1:cols])


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        grid = [tuple(map(int, line)) for line in map(list, file.read().splitlines())]

    rows, cols = len(grid), len(grid[0])
    coordinates = coordinates = product(range(rows), range(cols))

    print(sum([1 if visible(grid, *coord) else 0 for coord in coordinates]))


if __name__ == "__main__":
    main()
