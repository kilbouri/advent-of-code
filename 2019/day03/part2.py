from os import getcwd
import re as regex


def main():
    # open file and extract each move with regex for each wire (line)
    with open(f"{getcwd()}/2019/day03/input.txt", "r") as source:
        moves1 = regex.findall(r"(.)(\d+),", source.readline())
        moves2 = regex.findall(r"(.)(\d+),", source.readline())

    # each set represents the (x, y) points each wire crosses
    points1 = [(0, 0)]
    points2 = [(0, 0)]

    # we'll use a dictionary to look up distances travelled for each point
    distances1 = {}
    distances2 = {}

    moves = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    # determine all the points the first wire crosses
    distance = 0
    for move in moves1:
        char, count = move

        lastMove = points1[len(points1) - 1]
        dX, dY = moves[char]

        for i in range(int(count)):
            newPoint = (lastMove[0] + dX*(i+1), lastMove[1] + dY*(i+1))
            distance += 1

            if newPoint not in distances1.keys():
                distances1[newPoint] = distance

            points1.append(newPoint)
    points1 = set(points1)

    # determine all the points the second wire crosses
    distance = 0
    for move in moves2:
        char, count = move

        lastMove = points2[len(points2) - 1]
        dX, dY = moves[char]

        for i in range(int(count)):
            newPoint = (lastMove[0] + dX*(i+1), lastMove[1] + dY*(i+1))
            distance += 1

            if newPoint not in distances2.keys():
                distances2[newPoint] = distance

            points2.append(newPoint)
    points2 = set(points2)
    print("Point lists assembled. Comparing...")

    # intersect sets and remove (0, 0)
    intersections = list(points1 & points2)
    intersections.remove((0, 0))
    print("Intersections computed. Computing shortest distance...")

    # compute shortest distance
    shortestDistance = min(
        distances1[point] + distances2[point] for point in intersections)
    print("Shortest distance is: " + str(shortestDistance))


if __name__ == "__main__":
    main()
