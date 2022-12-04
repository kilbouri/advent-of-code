from os.path import dirname
import re


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as input:
        file = input.read()

    instructions = re.findall(r"(.)(\d+)", file)

    dN = 0
    dE = 0
    # (north, east)
    rotation = 90
    deltas = {
        0: [1, 0],
        90: [0, 1],
        180: [-1, 0],
        270: [0, -1]
    }

    for movement in instructions:
        action = movement[0]
        amount = int(movement[1])

        if action == "N":
            dN += amount
        elif action == "S":
            dN -= amount
        elif action == "E":
            dE += amount
        elif action == "W":
            dE -= amount
        elif action == "R":
            rotation = (rotation + amount) % 360
        elif action == "L":
            rotation = (rotation - amount) % 360
        elif action == "F":
            delta = deltas[rotation]
            dN += delta[0] * amount
            dE += delta[1] * amount

    print(abs(dN) + abs(dE))


if __name__ == "__main__":
    main()
