from os.path import dirname
import re
import math


def rotate(degrees: int, wp: list):
    newWaypoint = wp.copy()
    rads = math.radians(degrees)

    newWaypoint[1] = wp[1] * math.cos(rads) - wp[0] * math.sin(rads)
    newWaypoint[0] = wp[0] * math.cos(rads) + wp[1] * math.sin(rads)
    return newWaypoint


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as input:
        file = input.read()

    instructions = re.findall(r"(.)(\d+)", file)

    # (north, east)
    waypoint = [1, 10]
    dN = 0
    dE = 0

    for movement in instructions:
        action = movement[0]
        amount = int(movement[1])

        if action == "N":
            waypoint[0] += amount
        elif action == "S":
            waypoint[0] -= amount
        elif action == "E":
            waypoint[1] += amount
        elif action == "W":
            waypoint[1] -= amount

        elif action == "R":
            waypoint = rotate(-amount, waypoint)
        elif action == "L":
            waypoint = rotate(amount, waypoint)

        elif action == "F":
            dN += waypoint[0] * amount
            dE += waypoint[1] * amount

    print(abs(dN) + abs(dE))


if __name__ == "__main__":
    main()
