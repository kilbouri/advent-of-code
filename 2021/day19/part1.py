from os import getcwd
from itertools import product
from operator import sub, add
from functools import cache


@cache
def rotate(p, rx, ry, rz):
    # rotates point p rA times around the A axis
    x, y, z = p
    for _ in range(rx):
        x, y, z = x, z, -y
    for _ in range(ry):
        x, y, z = z, y, -x
    for _ in range(rz):
        x, y, z = y, -x, z
    return x, y, z


def match(originBeacons, beacons, threshold=12):
    # originBeacons: the beacons relative to the world origin
    # beacons: the beacons we want to try to match onto originBeacons
    # threshold: the min number of beacons that must overlap

    for rotation in product(range(4), repeat=3):
        rotatedBeacons = [rotate(b, *rotation) for b in beacons]
        for originBeacon in originBeacons:
            for beacon in rotatedBeacons:
                offset = tuple(map(sub, originBeacon, beacon))
                beaconsOffset = set(
                    tuple(map(add, b, offset))
                    for b in rotatedBeacons
                )
                if len(beaconsOffset & originBeacons) >= threshold:
                    return beaconsOffset


def main():
    with open(f"{getcwd()}/2021/day19/input.txt") as file:
        file = file.read().split("\n\n")
        scanners = list(map(lambda snnr: {
            tuple(map(int, coord.strip().split(",")))
            for coord in snnr.splitlines()[1:]
        }, file))

    visited = set()
    answer = set()

    def search(i, beacons):
        print(f"Matching {i}")
        answer.update(beacons)
        visited.add(i)

        for i, scanner in enumerate(scanners):
            if i in visited:
                continue

            matchRes = match(beacons, scanner)
            if matchRes:
                search(i, matchRes)

    search(0, scanners[0])
    print(len(answer))


if __name__ == "__main__":
    main()
