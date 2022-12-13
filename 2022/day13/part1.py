from bz2 import compress
from os.path import dirname
from pprint import pprint as print
from ast import literal_eval

IN_ORDER = 1
UNDECIDED = None
NOT_IN_ORDER = 0


def comparePackets(left, right) -> int | None:
    leftIsInt = isinstance(left, int)  # if false, it is a list
    rightIsInt = isinstance(right, int)  # if false, it is a list

    if leftIsInt and not rightIsInt:
        left = [left]
        leftIsInt = False
    elif rightIsInt and not leftIsInt:
        right = [right]
        rightIsInt = False

    if leftIsInt and rightIsInt:
        if left < right:
            return IN_ORDER
        if left > right:
            return NOT_IN_ORDER
        if left == right:
            return UNDECIDED

    # both are lists
    for newLeft, newRight in zip(left, right):
        result = comparePackets(newLeft, newRight)
        if result in [IN_ORDER, NOT_IN_ORDER]:
            return result

    if len(left) < len(right):
        return IN_ORDER
    if len(left) > len(right):
        return NOT_IN_ORDER

    return UNDECIDED


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        groups = [group.split('\n') for group in file.read().split('\n\n')]

    packetPairs = [tuple(map(literal_eval, [g for g in group if g])) for group in groups]
    outputs = [comparePackets(left, right) for left, right in packetPairs]

    print(sum([i for i, compResult in enumerate(outputs, start=1) if compResult == IN_ORDER]))


if __name__ == "__main__":
    main()
