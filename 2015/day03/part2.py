from os.path import dirname
from pprint import pprint as print


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        directions = file.read().strip()

    santas = [(0, 0)] * 2
    visitedHouses = {santas[0]}

    for i, direction in enumerate(directions):
        moveX, moveY = {
            '>': (1, 0),
            '<': (-1, 0),
            '^': (0, 1),
            'v': (0, -1)
        }[direction]

        santas[i % 2] = (santas[i % 2][0] + moveX, santas[i % 2][1] + moveY)
        visitedHouses.add(santas[i % 2])

    print(len(visitedHouses))


if __name__ == "__main__":
    main()
