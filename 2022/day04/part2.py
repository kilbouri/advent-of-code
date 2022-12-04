from os.path import dirname
from pprint import pprint as print

import re


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        lines = file.read().splitlines()

    # far from the fastest solution, but fast enough

    sections = [map(int, re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line).groups()) for line in lines]
    sectionRanges = [(range(r1Start, r1End + 1), range(r2Start, r2End + 1)) for r1Start, r1End, r2Start, r2End in sections]
    overlapSets = [set(range1) & set(range2) for range1, range2 in sectionRanges]
    actualOverlaps = [overlapSet for overlapSet in overlapSets if len(overlapSet) != 0]

    print(len(actualOverlaps))


if __name__ == "__main__":
    main()
