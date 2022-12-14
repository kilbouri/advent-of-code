from itertools import count
from os.path import dirname
from termcolor import colored


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        inpLines = file.read().splitlines()

    SPAWN_POINT = (500, 0)

    rockStructures = [[tuple(map(int, point.split(','))) for point in line.split(' -> ')] for line in inpLines]
    occupied = set()

    for rockStructure in rockStructures:
        for (ax, ay), (bx, by) in zip(rockStructure, rockStructure[1:]):
            if ax == bx:  # vertical line
                if ay > by:
                    ay, by = by, ay
                for y in range(ay, by + 1):
                    occupied.add((ax, y))
            else:  # horizontal line
                if ax > bx:
                    ax, bx = bx, ax
                for x in range(ax, bx + 1):
                    occupied.add((x, ay))

    # pretend there is a clipping boundary at the same Y level as the lowest point in the overall structure. If
    # a particle were to try to pass it, there is nothing below it to stop its motion.
    floor = max(y for _, y in occupied)

    def simulateNextParticle():
        # this closure makes the simulation logic a bit more concise and easier to follow.
        # It returns False iff the particle never comes to rest, otherwise True.

        px, py = SPAWN_POINT

        while True:
            if py > floor:
                return False  # we can't go down, the infinite floor is there
            elif (px + 0, py + 1) not in occupied:
                px, py = (px + 0, py + 1)
            elif (px - 1, py + 1) not in occupied:
                px, py = (px - 1, py + 1)
            elif (px + 1, py + 1) not in occupied:
                px, py = (px + 1, py + 1)
            else:
                break  # nowhere to move to, this is our resting point

        finalPoint = (px, py)

        occupied.add(finalPoint)
        return True  # are we occluding the spawn point?

    for numParticles in count(0):
        if not simulateNextParticle():
            break

    print(''.join([
        colored('A mountain of ', 'white'),
        colored(numParticles, 'yellow'),
        colored(' particles will have come to rest before they start flowing into the abyss. One heck of a mole hill.', 'white')
    ]))


if __name__ == "__main__":
    main()
