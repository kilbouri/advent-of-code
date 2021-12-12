from os import getcwd


def adjacent(x, y, maxX, maxY):
    return [
        (x + xs, y + ys)
        for xs, ys in [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if 0 <= x + xs < maxX and 0 <= y + ys < maxY
    ]


def main():
    with open(f"{getcwd()}/2021/day09/input.txt") as file:
        heightmap = [[c for c in line.strip()] for line in file]

    lowPoints = []

    for y, hl in enumerate(heightmap):
        for x, h in enumerate(hl):
            adjacents = adjacent(x, y, len(hl), len(heightmap))
            if all(heightmap[py][px] > h for px, py in adjacents):
                lowPoints.append(h)

    print(f"Total: {sum([int(x) + 1 for x in lowPoints])}")


if __name__ == "__main__":
    main()
