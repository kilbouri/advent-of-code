from os.path import dirname
from heapq import heappop, heappush
from itertools import product


def adjacent(x, y, maxX, maxY):
    return [
        (x + xs, y + ys)
        for xs, ys in ((1, 0), (0, 1), (-1, 0), (0, -1))
        if 0 <= x + xs < maxX and 0 <= y + ys < maxY
    ]


# Dijkstra's with a Priority Queue
# Part 1 uses a different solution because without the grid repetition,
# the shortest path only goes down and right. WIth the grid repetition,
# on my input data, it also goes right and up.
def minCost(costGrid):
    height = len(costGrid)
    width = len(costGrid[0])

    shortest = [[float("inf")] * width for _ in range(height)]
    queue = [(0, 0, 0)]

    while queue:
        dist, x, y = heappop(queue)

        for nx, ny in adjacent(x, y, width, height):
            newDistance = dist + costGrid[ny][nx]
            if shortest[ny][nx] > newDistance:
                shortest[ny][nx] = newDistance
                heappush(queue, (newDistance, nx, ny))

    return shortest[-1][-1]


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        file = file.readlines()

        def getWeight(w, x, y):
            a = w + x + y
            return (a - 1) % 9 + 1

        weights = [[int(w) for w in line.strip()] for line in file]
        weights = [
            [getWeight(w, x, y) for x in range(0, 5) for w in line]
            for y in range(0, 5) for line in weights
        ]
        weights[0][0] = 0

    print(f"The lowest risk path has a risk of {minCost(weights)}")


if __name__ == "__main__":
    main()
