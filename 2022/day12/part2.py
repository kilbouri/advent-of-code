from collections import deque
from os.path import dirname
from termcolor import colored


def toWeight(letter):
    if letter == 'S':
        return 1
    if letter == 'E':
        return 26

    return ord(letter) - ord('a') + 1


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        spaces = file.read().splitlines()
        weights = [[toWeight(letter) for letter in line] for line in spaces]

    ROWS, COLS = len(spaces), len(spaces[0])

    def bfsPathfind():
        queue = deque()

        for y in range(ROWS):
            for x in range(COLS):
                if spaces[y][x] in 'Sa':  # starting point and 'a' are both possible starting points
                    queue.append([(x, y), 0])

        visited = set()
        while queue:
            (x, y), distance = queue.popleft()
            if (x, y) in visited:
                continue

            visited.add((x, y))

            if spaces[y][x] == 'E':
                return distance

            for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                canX, canY = (x + dx, y + dy)

                if 0 <= canX < COLS and 0 <= canY < ROWS and weights[canY][canX] <= 1 + weights[y][x]:
                    # new position is in bounds and at most one elevation off of current
                    queue.append([(canX, canY), distance + 1])

    shortestTrailLength = bfsPathfind()
    print(''.join([
        colored('After lots of exploring, you know the best trail is ', 'grey'),
        colored(str(shortestTrailLength), 'yellow'),
        colored(' steps long. Break time!', 'grey')
    ]))


if __name__ == "__main__":
    main()
