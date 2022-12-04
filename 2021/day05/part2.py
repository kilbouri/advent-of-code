from os.path import dirname
from itertools import repeat


def sign(val):
    return val if val == 0 else (1 if val > 0 else -1)


def traceLine(line: str):
    pairs = line.strip().split(" -> ")

    sx, sy = map(int, pairs[0].split(","))
    ex, ey = map(int, pairs[1].split(","))
    dx, dy = sign(ex - sx), sign(ey - sy)

    xRange = range(sx, ex + dx, dx) if dx != 0 else repeat(sx)
    yRange = range(sy, ey + dy, dy) if dy != 0 else repeat(sy)

    return zip(xRange, yRange)


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        file = file.readlines()

    visitedPoints = {}

    for line in file:
        for point in traceLine(line):
            oldVal = visitedPoints.get(point, 0)
            visitedPoints[point] = oldVal + 1

    multiVisted = filter(lambda p: visitedPoints[p] >= 2, visitedPoints.keys())
    multiVisted = list(multiVisted)

    print(f"{len(multiVisted)} points overlapped.")


if __name__ == "__main__":
    main()
