from os.path import dirname
from pprint import pprint as print

import re


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        lines = file.read().splitlines()

    stacks = [
        list('GWLJBRTD'),
        list('CWS'),
        list('MTZR'),
        list('VPSHCTD'),
        list('ZDLTPG'),
        list('DCQJZRBF'),
        list('RTFMJDBS'),
        list('MVTBRHL'),
        list('VSDPQ'),
    ]

    for line in lines:
        parse = re.match(r'move (\d+) from (\d+) to (\d+)', line)
        count, source, dest = map(int, parse.groups())

        source = stacks[source - 1]
        dest = stacks[dest - 1]

        for _ in range(count):
            popped = source.pop(0)
            dest.insert(0, popped)

    print(''.join([stack[0] for stack in stacks]))


if __name__ == "__main__":
    main()
