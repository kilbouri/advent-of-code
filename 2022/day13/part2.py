from functools import cmp_to_key
from os.path import dirname
from termcolor import colored
from ast import literal_eval

IN_ORDER = -1
UNDECIDED = None
NOT_IN_ORDER = 1


def comparePackets(left, right):
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

    FIRST_MARKER = [[2]]
    SECOND_MARKER = [[6]]

    packets.append(FIRST_MARKER)
    packets.append(SECOND_MARKER)

    # works because values for IN_ORDER, NOT_IN_ORDER, UNDECIDED have been chosen to
    # conform to the cmp protocol
    packets.sort(key=cmp_to_key(comparePackets))

    decoderKey = (packets.index(FIRST_MARKER) + 1) * (packets.index(SECOND_MARKER) + 1)

    print(''.join([
        colored('With a headache from all the packet comparing, you find that ', 'white'),
        colored(decoderKey, 'yellow'),
        colored(' is the decoder key. It\'s naptime...', 'white')
    ]))


if __name__ == "__main__":
    main()
