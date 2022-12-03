from os import getcwd
from pprint import pprint as print

from string import ascii_letters


def main():
    with open(f"{getcwd()}/2022/day03/input.txt", "r") as file:
        sacks = file.read().splitlines()

    pouches = [(sack[:len(sack) // 2], sack[len(sack) // 2:]) for sack in sacks]

    pouchOverlaps = [set(pouchA).intersection(pouchB) for pouchA, pouchB in pouches]
    improperlyPackedItems = [tuple(mistakeSet)[0] for mistakeSet in pouchOverlaps]

    priorities = [ascii_letters.index(mistake) + 1 for mistake in improperlyPackedItems]
    print(sum(priorities))


if __name__ == "__main__":
    main()
