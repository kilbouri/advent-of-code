from os.path import dirname
from operator import mul
from functools import reduce


def adjacent(x, y, maxX, maxY):
    return [
        (x + xs, y + ys)
        for xs, ys in [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if 0 <= x + xs < maxX and 0 <= y + ys < maxY
    ]


def floodfill(x, y, visited, hmap):
    if hmap[y][x] < 9:
        visited.add((x, y))

    for nx, ny in adjacent(x, y, len(hmap[y]), len(hmap)):
        if hmap[y][x] < 9 and (nx, ny) not in visited:
            floodfill(nx, ny, visited, hmap)


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        heightmap = [[int(c) for c in line.strip()] for line in file]

    lowPoints = []
    basinSizes = []

    # find the lowest points in the heightmap
    for y, hl in enumerate(heightmap):
        for x, h in enumerate(hl):
            adjacents = adjacent(x, y, len(hl), len(heightmap))
            if all(heightmap[py][px] > h for px, py in adjacents):
                lowPoints.append(h)

    # compute the size of each basin surrounding each low point
    for point in lowPoints:
        basin = set()
        floodfill(point[1], point[2], basin, heightmap)
        basinSizes.append(len(basin))

    # sort basins by descending size, then print product of largest 3
    basinSizes = sorted(basinSizes, reverse=True)
    print(f"Total: {reduce(mul, basinSizes[:3])}")


if __name__ == "__main__":
    main()
