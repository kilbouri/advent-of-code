from os.path import dirname
from termcolor import colored

import re


def ensureTailConstraint(headX: int, headY: int, tailX: int, tailY: int):
    newTailX, newTailY = tailX, tailY

    deltaX, deltaY = tailX - headX, tailY - headY

    def sign(x): return -1 if x < 0 else 1 if x > 0 else 0

    if abs(deltaX) <= 1 and abs(deltaY) <= 1:
        pass  # this is OK. Condition required to prevent false positives below tho.
    elif abs(deltaX) > 1 and abs(deltaY) > 1:
        # we've moved diagonally
        newTailX = headX + sign(deltaX)
        newTailY = headY + sign(deltaY)
    elif abs(deltaX) > 1:
        # we moved to the right or left
        newTailX = headX + sign(deltaX)
        newTailY = headY
    elif abs(deltaY) > 1:
        # we moved up or down
        newTailY = headY + sign(deltaY)
        newTailX = headX

    return (newTailX, newTailY)


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    rawMoves = [re.match(r'(.) (\d+)', line).groups() for line in lines]
    moves = [(direction, int(amount)) for direction, amount in rawMoves]

    visited = {(0, 0)}
    knots = [(0, 0) for _ in range(10)]

    for direction, amount in moves:
        shiftX, shiftY = {
            'D': (0, -1),
            'U': (0, 1),
            'L': (-1, 0),
            'R': (1, 0)
        }[direction]

        for _ in range(amount):
            headX, headY = knots[0]

            # update head
            knots[0] = (headX + shiftX, headY + shiftY)

            # update the followers
            for i in range(1, len(knots)):
                knots[i] = ensureTailConstraint(*knots[i-1], *knots[i])

            # finally, update the visited set with the tail's position
            visited.add(knots[-1])

    print(''.join([
        colored('The tail of the longer rope visits ', 'white'),
        colored(len(visited), 'yellow'),
        colored(' positions.')
    ]))


if __name__ == "__main__":
    main()
