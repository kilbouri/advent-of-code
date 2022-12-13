from os.path import dirname
from ast import literal_eval
from termcolor import colored

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
        groups = file.read().split('\n\n')

    packetPairs = [(literal_eval(packet) for packet in group.split('\n') if packet) for group in groups]
    outputs = [comparePackets(left, right) for left, right in packetPairs]

    score = sum([i for i, compResult in enumerate(outputs, start=1) if compResult == IN_ORDER])

    print(''.join([
        colored('After lots of head scratching, you know the sum of the indices of the in-order packets is ', 'white'),
        colored(score, 'yellow'),
        colored('.', 'white')
    ]))


if __name__ == "__main__":
    main()
