from itertools import combinations
from os.path import dirname
from pprint import pprint as print


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    boxDimensions = [tuple(map(int, line.split('x'))) for line in lines]

    totalRibbonNeeded = 0

    for length, width, height in boxDimensions:
        perimiters = tuple(2 * (a + b) for a, b in combinations([length, width, height], r=2))
        volume = length * width * height

        totalRibbonNeeded += min(perimiters) + volume

    print(totalRibbonNeeded)


if __name__ == "__main__":
    main()
