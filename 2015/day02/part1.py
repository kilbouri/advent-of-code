from itertools import combinations
from os.path import dirname
from pprint import pprint as print


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    boxDimensions = [tuple(map(int, line.split('x'))) for line in lines]

    totalPaperNeeded = 0

    for length, width, height in boxDimensions:
        sides = tuple(a * b for a, b in combinations([length, width, height], r=2))
        totalPaperNeeded += 2 * sum(sides) + min(sides)  # smallest side as slack

    print(totalPaperNeeded)


if __name__ == "__main__":
    main()
