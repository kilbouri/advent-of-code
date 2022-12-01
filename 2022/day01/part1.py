from os import getcwd
from pprint import pprint as print


def main():
    with open(f'{getcwd()}/2022/day01/input.txt', 'r') as file:
        dwarves = map(lambda x: x.splitlines(), file.read().split('\n\n'))

    dwarfCals = map(lambda dwarf: sum(map(int, dwarf)), dwarves)
    print(max(dwarfCals))

if __name__ == "__main__":
    main()
