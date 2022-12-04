from os.path import dirname
import copy

# Z slice - the up/down in the pocket dimension
# Y slice - the up/down in each Z slice printed to the screen
# X slice - the left/right in each Z slice printed to the screen

cubeCorner1 = [-10, -10, -10]
cubeCorner2 = [10, 10, 10]


def getCube(pocket: dict, x: int, y: int, z: int) -> bool:
    return pocket[z][y][x] == "#"


def shouldBeActive(pocket: dict, x: int, y: int, z: int) -> bool:
    cubeState = getCube(pocket, x, y, z)

    adjacentActive = 0
    adjacentInactive = 0

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx == 0 and dy == 0 and dz == 0:
                    continue

                if getCube(pocket, x + dx, y + dy, z + dz):
                    adjacentActive += 1
                else:
                    adjacentInactive += 1

    if cubeState:
        if adjacentActive == 2 or adjacentActive == 3:
            return True
    else:
        if adjacentActive == 3:
            return True

    return False


def renderPocketDimension(pocket: dict) -> None:
    for z in range(cubeCorner1[0] + 1, cubeCorner2[0]):
        print(f"Z slice: {z}")
        for y in range(cubeCorner1[1] + 1, cubeCorner2[1]):
            for x in range(cubeCorner1[2] + 1, cubeCorner2[2]):
                if getCube(pocket, x, y, z):
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()


def simCycle(pocket: dict):
    newPocket = copy.deepcopy(pocket)

    for z in range(cubeCorner1[0] + 1, cubeCorner2[0]):
        for y in range(cubeCorner1[1] + 1, cubeCorner2[1]):
            for x in range(cubeCorner1[2] + 1, cubeCorner2[2]):
                sba = shouldBeActive(pocket, x, y, z)
                if sba:
                    newPocket[z][y][x] = "#"
                else:
                    newPocket[z][y][x] = "."

    return newPocket


def countActive(pocket: dict):
    active = 0
    for z in range(cubeCorner1[0] + 1, cubeCorner2[0]):
        for y in range(cubeCorner1[1] + 1, cubeCorner2[1]):
            for x in range(cubeCorner1[2] + 1, cubeCorner2[2]):
                if getCube(pocket, x, y, z):
                    active += 1
    return active


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        file = file.read()

    pocketDimension = {}
    for z in range(cubeCorner1[0], cubeCorner2[0] + 1):
        pocketDimension[z] = {}
        for y in range(cubeCorner1[1], cubeCorner2[1] + 1):
            pocketDimension[z][y] = {}
            for x in range(cubeCorner1[2], cubeCorner2[2] + 1):
                pocketDimension[z][y][x] = "."

    ySlices = file.split("\n")
    ySlice = {}
    for y, xSlice in enumerate(ySlices):
        for x, cube in enumerate(xSlice):
            pocketDimension[0][y-4][x-4] = cube

    for i in range(0, 6):
        pocketDimension = simCycle(pocketDimension)

    print(countActive(pocketDimension))


if __name__ == "__main__":
    main()
