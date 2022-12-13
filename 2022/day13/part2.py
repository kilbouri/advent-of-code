from bz2 import compress
from functools import cmp_to_key
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
        packets = [literal_eval(line) for line in file.read().splitlines() if line]

    packets.append([[2]])
    packets.append([[6]])

    def compare(left, right):
        comparison = comparePackets(left, right)
        if comparison == IN_ORDER:
            return -1
        else:
            return 1

    packets.sort(key=cmp_to_key(compare))
    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))


if __name__ == "__main__":
    main()
