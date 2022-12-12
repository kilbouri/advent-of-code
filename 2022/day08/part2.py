from os.path import dirname
from termcolor import colored
from itertools import product


def scenicScore(grid: list[list[int]], x: int, y: int):
    rows, cols = len(grid), len(grid[0])
    gridTranspose = list(zip(*grid))

    up = gridTranspose[x][0:y][::-1]
    down = gridTranspose[x][y+1:rows]
    left = grid[y][0:x][::-1]
    right = grid[y][x+1:cols]

    def viewDistance(direction: list[int]):
        for i, height in enumerate(direction):
            if height >= grid[y][x]:
                return i + 1

        return len(direction)

    return viewDistance(up) * viewDistance(down) * viewDistance(left) * viewDistance(right)


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        grid = [tuple(map(int, line)) for line in map(list, file.read().splitlines())]

    rows, cols = len(grid), len(grid[0])
    coordinates = product(range(rows), range(cols))

    bestTree = max([scenicScore(grid, *coord) for coord in coordinates])
    print(''.join([
        colored('The tree with the most scenic view has a score of ', 'white'),
        colored(bestTree, 'yellow'),
        colored(' points. What a view!', 'white')
    ]))


if __name__ == "__main__":
    main()
