from os.path import dirname
from pprint import pprint as print

from string import ascii_letters


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        sacks = file.read().splitlines()

    pouches = [(sack[:len(sack) // 2], sack[len(sack) // 2:]) for sack in sacks]
    pouchOverlaps = [set(pouchA) & set(pouchB) for pouchA, pouchB in pouches]
    improperlyPackedItems = [tuple(mistakeSet)[0] for mistakeSet in pouchOverlaps]

    priorities = [ascii_letters.index(mistake) + 1 for mistake in improperlyPackedItems]
    print(sum(priorities))


if __name__ == "__main__":
    main()
