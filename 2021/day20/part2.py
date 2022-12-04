from os.path import dirname
from itertools import product
from typing import Counter


def adjacent(x, y):
    for ys, xs in product(range(-1, 2), repeat=2):
        yield (x + xs, y + ys)


def getBounds(image):
    return (
        min(p[0] for p in image),
        max(p[0] for p in image),
        min(p[1] for p in image),
        max(p[1] for p in image)
    )


def pointsInImage(image):
    # +/- 1 to account for pixels that may become lit
    # during enhancement
    bounds = getBounds(image)
    imgMinX = bounds[0] - 2
    imgMaxX = bounds[1] + 2
    imgMinY = bounds[2] - 2
    imgMaxY = bounds[3] + 2

    for y in range(imgMinY, imgMaxY + 1):
        for x in range(imgMinX, imgMaxX + 1):
            yield x, y


def enhance(image: dict, algorithm, default):
    newImage = dict()

    def calculate(x, y):
        binStr = []
        for adj in adjacent(x, y):
            pix = image.get(adj, default)
            binStr += '1' if pix == '#' else '0'

        idx = int("".join(binStr), 2)
        return algorithm[idx]

    for x, y in pointsInImage(image):
        newImage[(x, y)] = calculate(x, y)

    return newImage


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        file = file.read().split("\n\n")

        algo = file[0]
        image = {
            (x, y): pix
            for y, line in enumerate(file[1].strip().splitlines())
            for x, pix in enumerate(line)
        }

    for itr in range(50):
        print(itr)
        # account for algo[0] = '#' inputs
        default = algo[0] if itr % 2 != 0 else '.'
        image = enhance(image, algo, default)

    lit = Counter(image.values())["#"]

    print(f"There are {lit} bright pixels in the result")


if __name__ == "__main__":
    main()
