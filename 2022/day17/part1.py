from os.path import dirname


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        jets = file.read().strip()

    tetrisBoard = {(x, 0) for x in range(7)}

    def getPiecePointSet(type, blockY):
        # Type is 0-indexed and in order of spawning to make it easy to compute which to spawn
        return {
            0: {(2, blockY), (3, blockY), (4, blockY), (5, blockY)},  # Horizontal Piece
            1: {(3, blockY + 2), (2, blockY + 1), (3, blockY + 1), (4, blockY + 1), (3, blockY)},  # Plus Piece
            2: {(2, blockY), (3, blockY), (4, blockY), (4, blockY + 1), (4, blockY + 2)},  # L Piece
            3: {(2, blockY), (2, blockY + 1), (2, blockY + 2), (2, blockY + 3)},  # Vertical Piece
            4: {(2, blockY + 1), (2, blockY), (3, blockY + 1), (3, blockY)}  # Square Piece
        }[type]

    def moveLeft(piece):
        if any(x == 0 for x, _ in piece):
            return piece
        return {(x - 1, y) for x, y in piece}

    def moveRight(piece):
        if any(x == 6 for x, _ in piece):
            return piece
        return {(x + 1, y) for x, y in piece}

    def moveDown(piece):
        return {(x, y - 1) for x, y in piece}

    def moveUp(piece):
        return {(x, y + 1) for x, y in piece}

    SIMULATION_LENGTH = 2022
    top = time = 0

    for numRocksFallen in range(SIMULATION_LENGTH):
        piece = getPiecePointSet(numRocksFallen % 5, top + 4)

        while not piece & tetrisBoard:
            # jet effect
            if jets[time % len(jets)] == '<':
                piece = moveLeft(piece)

                # un-move if this caused us to overlap with something else
                if piece & tetrisBoard:
                    piece = moveRight(piece)
            else:
                piece = moveRight(piece)

                # un-move if this caused us to overlap with something else
                if piece & tetrisBoard:
                    piece = moveLeft(piece)

            time += 1
            piece = moveDown(piece)

        piece = moveUp(piece)  # the last downward move caused a collision, we need to undo that
        tetrisBoard |= piece  # set the piece into the board
        top = max(y for _, y in tetrisBoard)  # calculate new board top (may not be the top of the piece!)

    print(top)


if __name__ == "__main__":
    main()
