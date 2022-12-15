from os.path import dirname
from termcolor import colored

import re


def parseSensorBeaconPair(text):
    pattern = r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)'
    sensorX, sensorY, beaconX, beaconY = map(int, re.match(pattern, text).groups())

    return ((sensorX, sensorY), (beaconX, beaconY))


def manhattanDistance(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2

    dx = abs(p1x - p2x)
    dy = abs(p1y - p2y)

    return dx + dy


def getCoveredRange(sensor, beacon, ylevel):
    # Any distance travelled in the Y direction to get to the y level restricts
    # how far the sensor can read in the X direction.

    maxDist = manhattanDistance(sensor, beacon)
    yDist = abs(ylevel - sensor[1])
    maxXDelta = max(0, maxDist - yDist)

    return (sensor[0] - maxXDelta, sensor[0] + maxXDelta)


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    Y_LEVEL = 2000000

    sensorBeaconPairs = [parseSensorBeaconPair(line) for line in lines]

    freeXCoordinates = set()

    for sensor, beacon in sensorBeaconPairs:
        coveredMin, coveredMax = getCoveredRange(sensor, beacon, Y_LEVEL)

        freeXCoordinates |= set(range(coveredMin, coveredMax))

        # Some inputs may have beacons that are on the same Y as we are concerned with.
        # Their X coordinates must be removed because there is in fact a beacon there!
        bx, by = beacon
        if by == Y_LEVEL:
            freeXCoordinates -= {bx}

    result = len(freeXCoordinates)

    print(''.join([
        colored('You careful counting, you conclude that ', 'white'),
        colored(result, 'yellow'),
        colored(f' positions at Y={Y_LEVEL} cannot contain a beacon.', 'white')
    ]))


if __name__ == "__main__":
    main()
