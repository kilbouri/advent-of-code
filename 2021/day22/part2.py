from os import getcwd
from re import findall
from re import match


def parseStep(line):
    state = match(r"(on|off)", line).groups()[0]
    x1, x2, y1, y2, z1, z2 = map(int, findall(r"(-?\d+)", line))

    return state, (x1, x2), (y1, y2), (z1, z2)


def main():
    with open(f"{getcwd()}/2021/day22/input.txt") as file:
        file = file.readlines()
        steps = list(map(parseStep, file))

    # lists of each axes' critical values (values that on the boundary of regions)
    critX = []
    critY = []
    critZ = []

    for step in steps:
        _, x, y, z = step
        critX.append(x[0])
        critX.append(x[1] + 1)
        critY.append(y[0])
        critY.append(y[1] + 1)
        critZ.append(z[0])
        critZ.append(z[1] + 1)

    steps.reverse()
    critX.sort()
    critY.sort()
    critZ.sort()

    # now we iterate over all regions, adding the volume of each "on" region
    total = 0
    for x1, x2 in zip(critX, critX[1:]):
        print(f"Tallying x={x1} .. {x2}")
        xRegs = [v for v in steps if v[1][0] <= x1 <= v[1][1]]

        for y1, y2 in zip(critY, critY[1:]):
            yRegs = [v for v in xRegs if v[2][0] <= y1 <= v[2][1]]

            for z1, z2 in zip(critZ, critZ[1:]):
                if next((s == "on" for s, _, _, z in yRegs if z[0] <= z1 <= z[1]), False):
                    total += (x2 - x1) * (y2 - y1) * (z2 - z1)

    print(f"{total} cubes are left on")


if __name__ == "__main__":
    main()
