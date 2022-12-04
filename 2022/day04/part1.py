from os.path import dirname
from pprint import pprint as print

import re


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        lines = file.read().splitlines()

    sections = [re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line).groups() for line in lines]

    counter = 0
    for section in sections:
        r1Start, r1End, r2Start, r2End = map(int, section)

        r1ContainsR2 = r1Start <= r2Start and r2End <= r1End
        r2ContainsR1 = r2Start <= r1Start and r1End <= r2End

        if r1ContainsR2 or r2ContainsR1:
            counter += 1

    print(counter)


if __name__ == "__main__":
    main()
