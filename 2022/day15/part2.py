from os.path import dirname
from termcolor import colored

import z3
import re


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    # Closure to make the parsing code easier to read
    def parseSensorBeaconPair(text) -> tuple[tuple[int, int], tuple[int, int]]:
        pattern = r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)'
        sensorX, sensorY, beaconX, beaconY = map(int, re.match(pattern, text).groups())

        return ((sensorX, sensorY), (beaconX, beaconY))

    MAX_BOUND = 4000000

    sensorBeaconPairs = [parseSensorBeaconPair(line) for line in lines]

    # the input space is too big, we need to be very smart about this... what's smarter than a SAT Solver?
    solver = z3.Solver()

    # X and Y are ints, within [0, MAX_BOUND]
    x, y = z3.Int('x'), z3.Int('y')

    solver.add(x >= 0)
    solver.add(x <= MAX_BOUND)

    solver.add(y >= 0)
    solver.add(y <= MAX_BOUND)

    for (sensorX, sensorY), (beaconX, beaconY) in sensorBeaconPairs:
        # X, Y cannot have manhattan distance closer than closest beacon
        solverDistance = z3.Abs(sensorX - x) + z3.Abs(sensorY - y)
        beaconDistance = abs(sensorX - beaconX) + abs(sensorY - beaconY)

        solver.add(solverDistance > beaconDistance)

        # X, Y cannot be the same as the beacon
        solver.add(z3.And(x != beaconX, y != beaconY))

    assert solver.check() == z3.sat  # ensure the problem can actually be solved, error if not
    model = solver.model()  # grab the solution (aka model) it found in the last check() call

    finalX = model[x].as_long()
    finalY = model[y].as_long()

    result = MAX_BOUND * finalX + finalY  # a 2D-as-1D-array conversion! Neat!

    print(''.join([
        colored(f'After "fancy trial and error", you find the missing beacon is at {(finalX, finalY)}, for a tuning frequency of ', 'white'),
        colored(result, 'yellow'),
        colored('. Good thing Elves can\'t hear such high frequencies.', 'white')
    ]))


if __name__ == "__main__":
    main()
