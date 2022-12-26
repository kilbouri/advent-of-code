from dataclasses import dataclass
from functools import cache
from os.path import dirname

import re


@dataclass
class Tile:
    FACING_RIGHT = 0
    FACING_DOWN = 1
    FACING_LEFT = 2
    FACING_UP = 3
    FACING_UNCHANGED = -1

    x: int
    y: int
    isWall: bool

    # left/right/up/down are tuples of the form (position, newFacing).
    left: tuple["Tile", int] | None = None
    right: tuple["Tile", int] | None = None
    up: tuple["Tile", int] | None = None
    down: tuple["Tile", int] | None = None

    def neighbour(self, facing):
        return {
            0: self.right,
            1: self.down,
            2: self.left,
            3: self.up
        }[facing]


def main():
    # NOTE: if you want to use the test file, you have to re-write the
    # tile linking pass cuz it depends on the face layout in the input
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        board, instructions = file.read().split('\n\n')
        board = board.splitlines()

    SIDE_LENGTH = 50

    tiles: dict[tuple[int, int], Tile] = {}

    position: Tile | None = None
    facing = 0

    for y, line in enumerate(board):
        for x, character in enumerate(line):
            if character == " ":
                # Skip empty (out of bounds) spaces
                continue

            tile = Tile(x + 1, y + 1, character == '#')
            tiles[(x + 1, y + 1)] = tile

            # Since we iterate from bottom to top, left to right, the first tile we
            # create will be the starting point
            position = tile if position is None else position

    # Second pass to assign left/right/up/down as possible for each tile
    for tile in tiles.values():

        # Update tile left
        if (tile.x - 1, tile.y) in tiles:
            tile.left = tiles[(tile.x - 1, tile.y)], Tile.FACING_UNCHANGED
        else:
            if tile.y in range(1, SIDE_LENGTH + 1):
                tile.left = tiles[(1, SIDE_LENGTH + 1 - tile.y + 2 * SIDE_LENGTH)], Tile.FACING_RIGHT
            elif tile.y in range(SIDE_LENGTH + 1, 2 * SIDE_LENGTH + 1):
                tile.left = tiles[(tile.y - SIDE_LENGTH, 2 * SIDE_LENGTH + 1)], Tile.FACING_DOWN
            elif tile.y in range(2 * SIDE_LENGTH + 1, 3 * SIDE_LENGTH + 1):
                tile.left = tiles[(SIDE_LENGTH + 1, 3 * SIDE_LENGTH + 1 - tile.y)], Tile.FACING_RIGHT
            else:
                tile.left = tiles[(tile.y - 2 * SIDE_LENGTH, 1)], Tile.FACING_DOWN

        # Update tile right
        if (tile.x + 1, tile.y) in tiles:
            tile.right = tiles[(tile.x + 1, tile.y)], Tile.FACING_UNCHANGED
        else:
            if tile.y in range(1, SIDE_LENGTH + 1):
                tile.right = tiles[(2 * SIDE_LENGTH, SIDE_LENGTH + 1 - tile.y + 2 * SIDE_LENGTH)], Tile.FACING_LEFT
            elif tile.y in range(SIDE_LENGTH + 1, 2 * SIDE_LENGTH + 1):
                tile.right = tiles[(tile.y + SIDE_LENGTH, SIDE_LENGTH)], Tile.FACING_UP
            elif tile.y in range(2 * SIDE_LENGTH + 1, 3 * SIDE_LENGTH + 1):
                tile.right = tiles[(3 * SIDE_LENGTH, 3 * SIDE_LENGTH + 1 - tile.y)], Tile.FACING_LEFT
            else:
                tile.right = tiles[(tile.y - 2 * SIDE_LENGTH, 3 * SIDE_LENGTH)], Tile.FACING_UP

        # Update tile up
        if (tile.x, tile.y - 1) in tiles:
            tile.up = tiles[(tile.x, tile.y - 1)], Tile.FACING_UNCHANGED
        else:
            if tile.x in range(1, SIDE_LENGTH + 1):
                tile.up = tiles[(SIDE_LENGTH + 1, tile.x + SIDE_LENGTH)], Tile.FACING_RIGHT
            elif tile.x in range(SIDE_LENGTH + 1, 2 * SIDE_LENGTH + 1):
                tile.up = tiles[(1, tile.x + 2 * SIDE_LENGTH)], Tile.FACING_RIGHT
            else:
                tile.up = tiles[(tile.x - 2 * SIDE_LENGTH, 4 * SIDE_LENGTH)], Tile.FACING_UNCHANGED

        # Update tile down
        if (tile.x, tile.y + 1) in tiles:
            tile.down = tiles[(tile.x, tile.y + 1)], Tile.FACING_UNCHANGED
        else:
            if tile.x in range(1, SIDE_LENGTH + 1):
                tile.down = tiles[(tile.x + 2 * SIDE_LENGTH, 1)], Tile.FACING_UNCHANGED
            elif tile.x in range(SIDE_LENGTH + 1, 2 * SIDE_LENGTH + 1):
                tile.down = tiles[(SIDE_LENGTH, tile.x + 2 * SIDE_LENGTH)], Tile.FACING_LEFT
            else:
                tile.down = tiles[(2 * SIDE_LENGTH, tile.x - SIDE_LENGTH)], Tile.FACING_LEFT

    for command in re.findall(r"(\d+|[A-Z])", instructions):
        if command.isdigit():
            # This is a number of steps to move
            for _ in range(int(command)):
                neighbour = position.neighbour(facing)

                if neighbour is None:
                    assert False, \
                        "Found a tile with no neighbour in the direction we are facing"

                nextTile, nextFacing = neighbour
                if nextTile.isWall:
                    break  # can no longer move forward

                position = nextTile
                if nextFacing != Tile.FACING_UNCHANGED:
                    facing = nextFacing

        else:
            # This is a rotation command
            delta = -1 if command == 'L' else 1
            facing = (facing + delta) % 4

    print(position.y * 1000 + position.x * 4 + facing)


if __name__ == "__main__":
    main()
