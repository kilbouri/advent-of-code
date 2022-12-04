from os.path import dirname
from itertools import count, product


def adjacent(x, y, maxX, maxY):
    return [
        (x + xs, y + ys)
        for xs, ys in product(range(-1, 2), range(-1, 2))
        if 0 <= x + xs < maxX and 0 <= y + ys < maxY and not xs == ys == 0
    ]


def flash(x, y, octos, flashed):
    if flashed[y][x]:
        return 0

    # flash octo, then increment each adjacent octo
    flashed[y][x] = 1
    for u, v in adjacent(x, y, len(octos[y]), len(octos)):
        octos[v][u] += 1

        # flash adjacent octo if needed
        if octos[v][u] > 9:
            flash(u, v, octos, flashed)


def simulateStep(octos):
    flashed = [[0 for _ in line] for line in octos]

    # increase energy of all octos by 1
    for y, line in enumerate(octos):
        for x, octo in enumerate(line):
            octos[y][x] += 1

    # flash any octos over 9 energy
    for y, line in enumerate(octos):
        for x, octo in enumerate(line):
            if octo > 9:
                flash(x, y, octos, flashed)

    # reset energy of any octo that flashed
    for y, line in enumerate(flashed):
        for x, octoFlashed in enumerate(line):
            # octoFlashed is 1 when flashed, 0 otherwise
            octos[y][x] *= 1 - octoFlashed

    # count the number of octopi that flashed in this step
    return sum(sum(line) for line in flashed)


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        octos = [
            list(map(int, [c for c in line.strip()]))
            for line in file.readlines()
        ]

    for step in count(start=1):
        if simulateStep(octos) == len(octos) * len(octos[0]):
            print(f"The octopi flashed in sync on step {step}.")
            break


if __name__ == "__main__":
    main()
