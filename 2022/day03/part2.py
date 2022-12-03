from os import getcwd
from pprint import pprint as print

from string import ascii_letters


def main():
    with open(f"{getcwd()}/2022/day03/input.txt", "r") as file:
        sacks = file.read().splitlines()

    elfGroups = [tuple(sacks[i:i+3]) for i in range(0, len(sacks), 3)]
    badgeTypes = [tuple(set(a) & set(b) & set(c))[0] for a, b, c in elfGroups]
    priorities = [ascii_letters.index(item) + 1 for item in badgeTypes]

    print(sum(priorities))


if __name__ == "__main__":
    main()
