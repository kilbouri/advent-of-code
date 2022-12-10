from os.path import dirname
from pprint import pprint as print


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        directions = file.read().strip()

    santaX, santaY = (0, 0)
    visitedHouses = {(santaX, santaY)}

    for direction in directions:
        moveX, moveY = {
            '>': (1, 0),
            '<': (-1, 0),
            '^': (0, 1),
            'v': (0, -1)
        }[direction]

        santaX += moveX
        santaY += moveY

        visitedHouses.add((santaX, santaY))

    print(len(visitedHouses))


if __name__ == "__main__":
    main()
