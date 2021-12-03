from os import getcwd
import copy


def getIndex(source, x, y):
    if 0 > x or x >= len(source):
        return None
    elif 0 > y or y >= len(source[x]):
        return None
    else:
        return source[x][y]


def checkSurroundings(seats, x, y):

    occupiedCount = 0
    for dX in range(-1, 2):
        for dY in range(-1, 2):

            if dX == 0 and dY == 0:
                continue

            delta = [dX, dY]
            while getIndex(seats, x + delta[0], y + delta[1]) == ".":
                delta[0] += dX
                delta[1] += dY

            if getIndex(seats, x + delta[0], y + delta[1]) == "#":
                occupiedCount += 1

    return occupiedCount


def applyRules(seats):

    newSeats = copy.deepcopy(seats)
    changeCount = 0

    for x in range(len(seats)):
        for y in range(len(seats[x])):

            surroundings = checkSurroundings(seats, x, y)
            if seats[x][y] == "L" and surroundings == 0:
                newSeats[x][y] = "#"  # occupado

            elif seats[x][y] == "#" and surroundings >= 5:
                newSeats[x][y] = "L"  # deoccupado

            else:
                continue

            changeCount += 1  # if reached, neither of the change rules were met
    return (newSeats, changeCount)


def main():
    with open(f"{getcwd()}/2020/day11/input.txt", "r") as input:
        rows = list(input.read().split())
        seats = list(map(list, rows))

    seats = (seats, 1)
    while True:
        seats = applyRules(seats[0])

        if seats[1] == 0:
            break

    # count the number of occupado seats
    seats = seats[0]
    seatsLen = len(seats)

    print(sum(seats[i].count("#") for i in range(seatsLen)))


if __name__ == "__main__":
    main()
