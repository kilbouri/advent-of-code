from os.path import dirname
from pprint import pprint as print


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        dwarves = map(lambda x: x.splitlines(), file.read().split('\n\n'))

    dwarfCals = sorted(map(lambda dwarf: sum(map(int, dwarf)), dwarves), reverse=True)
    print(sum(dwarfCals[:3]))


if __name__ == "__main__":
    main()
