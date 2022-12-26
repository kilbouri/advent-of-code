from functools import cache
from os.path import dirname

import re


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        tiles, instructions = file.read().split('\n\n')

    tiles = list(map(list, tiles.splitlines()))

    amounts = list(map(int, reversed(re.findall(r'\d+', instructions))))
    rotations = list(reversed(re.findall(r'[LR]', instructions)))

    position = (min(x for x, value in enumerate(tiles[0]) if value == '.'), 0)
    delta = (1, 0)  # facing right

    @cache
    def wrapAround(pos, delta):
        dx, dy = map(lambda x: -x, delta)

        wrappedX, wrappedY = pos
        while True:
            testX, testY = wrappedX + dx, wrappedY + dy

            if testY < 0 or testY >= len(tiles):
                return wrappedX, wrappedY

            if testX < 0 or testX >= len(tiles[testY]):
                return wrappedX, wrappedY

            newTile = tiles[testY][testX]
            if newTile == ' ':
                return wrappedX, wrappedY

            wrappedX, wrappedY = testX, testY

    def rotateCW(delta):
        dx, dy = delta
        return (-dy, dx)

    def rotateCCW(delta):
        dx, dy = delta
        return (dy, -dx)

    def forward(position, direction, amount):

        for _ in range(amount):
            px, py = position
            dx, dy = direction

            newX, newY = (px + dx, py + dy)

            if newY < 0 or newY >= len(tiles):
                newX, newY = wrapAround((newX, newY), direction)
            elif newX < 0 or newX >= len(tiles[newY]):
                newX, newY = wrapAround((newX, newY), direction)

            newTile = tiles[newY][newX]

            if newTile == ' ':
                newX, newY = wrapAround((newX, newY), direction)

            if newTile == '#':
                return position

            position = (newX, newY)

        return position

    for t in range(len(amounts) + len(rotations)):
        if t % 2 == 0:
            amount = amounts.pop()
            position = forward(position, delta, amount)
        else:
            rotation = rotations.pop()
            if rotation == 'L':
                delta = rotateCCW(delta)
            else:
                delta = rotateCW(delta)

    # we use zero indexes, but the problem does not
    finalRow, finalCol = position[1] + 1, position[0] + 1

    facing = {
        (1, 0): 0,
        (-1, 0): 2,
        (0, -1): 3,
        (0, 1): 1
    }[delta]

    print(sum([finalRow * 1000, finalCol * 4, facing]))


if __name__ == "__main__":
    main()
