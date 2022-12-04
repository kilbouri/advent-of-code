from os.path import dirname
from re import findall
from re import match
from collections import defaultdict
from pprint import pprint


def parseStep(line):
    state = match(r"(on|off)", line).groups()[0]
    nums = list(map(int, findall(r"(-?\d+)", line)))

    return state == "on", nums


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        file = file.readlines()
        steps = map(parseStep, file)

    reactor = defaultdict(bool)

    i = 0
    for state, ranges in steps:
        print(f"Step {i}")
        i += 1
        for x in range(ranges[0], ranges[1] + 1):
            if -50 <= x <= 50:
                for y in range(ranges[2], ranges[3] + 1):
                    if -50 <= y <= 50:
                        for z in range(ranges[4], ranges[5] + 1):
                            if -50 <= z <= 50:
                                reactor[x, y, z] = state

    pprint(len(list(filter(lambda x: x, reactor.values()))))


if __name__ == "__main__":
    main()
