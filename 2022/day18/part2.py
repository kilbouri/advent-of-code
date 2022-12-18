from collections import deque
import functools
from itertools import product
from os.path import dirname


def adjacent(x, y, z):
    for dx, dy, dz in product([-1, 0, 1], repeat=3):
        if sum(map(abs, [dx, dy, dz])) == 1:
            yield x + dx, y + dy, z + dz


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    droplet = {tuple(map(int, line.split(','))) for line in lines}

    # increment/decrement ensures the bounds include at least one cube of air on all sides
    minX, maxX = min(x for x, _, _ in droplet) - 1, max(x for x, _, _ in droplet) + 1
    minY, maxY = min(y for _, y, _ in droplet) - 1, max(y for _, y, _ in droplet) + 1
    minZ, maxZ = min(z for _, _, z in droplet) - 1, max(z for _, _, z in droplet) + 1

    outsidePoint = (minX, minY, minZ)
    outsideDroplet = set()  # will also double as our "visited" set for BFS floodfill below

    # standard BFS-based floodfill
    queue = deque(tuple([outsidePoint]))  # I hate *args call syntax sometimes

    while queue:
        point = queue.pop()
        outsideDroplet.add(point)

        queue.extend(
            point
            for point in adjacent(*point)
            if point not in outsideDroplet and point not in droplet and point not in queue
            if minX <= point[0] <= maxX and minY <= point[1] <= maxY and minZ <= point[2] <= maxZ
        )

    # solidDroplet is calculated by solidCube - outsideDroplet. To save memory by avoiding allocating
    # a set for solidCube, we use a generator of points in the cube and set comprehension to remove any
    # points in outsideDroplet.
    solidCube = product(range(minX, maxX + 1), range(minY, maxY + 1), range(minZ, maxZ + 1))
    solidDroplet = {point for point in solidCube if point not in outsideDroplet}

    # Code yoinked from part 1 for calculating the surface area of the droplet. This time the droplet
    # contains no voids so the surface area is only the exterior surface area.

    surfaceArea = 0
    for point in solidDroplet:
        surfaceArea += len([adjPoint for adjPoint in adjacent(*point) if adjPoint not in solidDroplet])

    print(surfaceArea)


if __name__ == "__main__":
    main()
