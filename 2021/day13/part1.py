from os.path import dirname


def fold(points, instruction: str):
    # grab fold axis and index from string
    axis, coord = instruction[11:].split("=")
    coord = int(coord)

    # an X-fold is just the transpose of a Y-fold
    points = [list(e) for e in zip(*points)] if axis == 'x' else points

    # do a Y-fold
    folded = points[:coord]
    for y, row in enumerate(points[coord + 1:], start=1):
        if y <= len(folded):
            for x, val in enumerate(row):
                folded[-y][x] |= val

    # undo the transpose that converted an X-fold to a Y-fold
    folded = [list(e) for e in zip(*folded)] if axis == 'x' else folded

    return folded


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        file = file.read().split('\n\n')

        points = [list(map(int, s.strip().split(',')))
                  for s in file[0].splitlines()]

        foldInst = file[1].splitlines()

    width = max([p[0] for p in points])
    height = max([p[1] for p in points])

    paper = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
    for point in points:
        paper[point[1]][point[0]] = 1

    folded = fold(paper, foldInst[0])

    answer = sum([sum(line) for line in folded])
    print(f"{answer} dots are visible.")


if __name__ == "__main__":
    main()
