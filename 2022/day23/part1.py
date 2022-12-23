from itertools import product
from os.path import dirname


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        grove = [list(line) for line in file.read().splitlines()]

    elves = {(x, y) for y, x in product(range(len(grove)), range(len(grove[0]))) if grove[y][x] == '#'}

    NUM_ROUNDS = 10

    NORTH = 0
    SOUTH = 1
    WEST = 2
    EAST = 3

    directionOrder = [NORTH, SOUTH, WEST, EAST]

    def canMoveInDirection(elfX, elfY, direction):
        delta = {
            NORTH: [(-1, -1), (0, -1), (1, -1)],
            SOUTH: [(-1, 1), (0, 1), (1, 1)],
            WEST: [(-1, -1), (-1, 0), (-1, 1)],
            EAST: [(1, -1), (1, 0), (1, 1)]
        }[direction]

        return all((elfX + dx, elfY + dy) not in elves for dx, dy in delta)

    def moveInDirection(elfX, elfY, direction):
        if direction == NORTH:
            return (elfX, elfY - 1)
        if direction == SOUTH:
            return (elfX, elfY + 1)
        if direction == WEST:
            return (elfX - 1, elfY)
        if direction == EAST:
            return (elfX + 1, elfY)

    def boundingRect(points):
        minX = min(x for x, _ in points)
        maxX = max(x for x, _ in points)
        minY = min(y for _, y in points)
        maxY = max(y for _, y in points)

        return (minX, minY), (maxX, maxY)

    for _ in range(NUM_ROUNDS):
        # first half - elves propose new positions
        propositions = dict()  # keeps track of which elves want to move to a given position

        for elf in elves:
            possibleDirections = [direction for direction in directionOrder if canMoveInDirection(*elf, direction)]
            if len(possibleDirections) == len(directionOrder):
                # elf does nothing if none of the 8 adjacent locations are occupied (this just happens
                # to be representable by having all possible directions as candidates)
                continue

            if len(possibleDirections) == 0:
                # no direction was movable, so the elf must stay put
                continue

            # since we used directionOrder in the above listcomp, the first value is the first
            # direction that the elf would try to move that it can actually move to
            chosenDireciton = possibleDirections[0]

            newPosition = moveInDirection(*elf, chosenDireciton)
            if newPosition not in propositions:
                propositions[newPosition] = [elf]
            else:
                propositions[newPosition].append(elf)

        # second half - elves move to their proposed position IFF they were the only one to propose that position
        for newPosition, proposingElves in propositions.items():
            if len(proposingElves) != 1:
                # elves don't move if any other elf also proposed moving to the same position
                continue

            # perform the move
            elves.remove(proposingElves[0])
            elves.add(newPosition)

        # end-of-round action - rotate the direction order
        directionOrder.append(directionOrder.pop(0))

    (minX, minY), (maxX, maxY) = boundingRect(elves)

    # The number of open ground spaces in the bounding rectangle is its area
    # minus the number of elves, since each elf is at a unique location.
    # The +1 is required as otherwise the bound would be upper-exclusive.
    width, height = (maxX - minX + 1), (maxY - minY + 1)
    openLocations = width * height - len(elves)

    print(openLocations)


if __name__ == "__main__":
    main()
