from os.path import dirname


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        jets = file.read().strip()

    board = {(x, 0) for x in range(7)}

    def getPiecePointSet(type, blockY):
        # Type is 0-indexed and in order of spawning to make it easy to compute which to spawn
        return [
            {(2, blockY), (3, blockY), (4, blockY), (5, blockY)},  # Horizontal Piece
            {(3, blockY + 2), (2, blockY + 1), (3, blockY + 1), (4, blockY + 1), (3, blockY)},  # Plus Piece
            {(2, blockY), (3, blockY), (4, blockY), (4, blockY + 1), (4, blockY + 2)},  # L Piece
            {(2, blockY), (2, blockY + 1), (2, blockY + 2), (2, blockY + 3)},  # Vertical Piece
            {(2, blockY + 1), (2, blockY), (3, blockY + 1), (3, blockY)}  # Square Piece
        ][type]

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

    SIMULATION_LENGTH = 1_000_000_000_000

    jetIndex = rocksFallen = 0
    seenStates = {}
    totalHeight = 0

    while rocksFallen < SIMULATION_LENGTH:
        print(f'\r{rocksFallen / SIMULATION_LENGTH * 100:0.9f}%', end='')

        top = max(y for _, y in board)
        blockType = rocksFallen % 5

        piece = getPiecePointSet(blockType, top + 4)

        while True:
            # jet effect
            if jets[jetIndex] == '<':
                piece = moveLeft(piece)

                # un-move if this caused us to overlap with something else
                if piece & board:
                    piece = moveRight(piece)
            else:
                piece = moveRight(piece)

                # un-move if this caused us to overlap with something else
                if piece & board:
                    piece = moveLeft(piece)

            jetIndex = (jetIndex + 1) % len(jets)
            piece = moveDown(piece)

            if piece & board:
                piece = moveUp(piece)  # the last downward move caused a collision, we need to undo that
                board |= piece  # set the piece into the board

                oldTop = top
                top = max(y for _, y in board)
                totalHeight += top - oldTop

                # Little bit of cycle detection... lets us skip 99.999999% of the iterations as
                # soon as we find one :D
                summary = (jetIndex, blockType, frozenset((x, top - y) for x, y, in board if top - y <= 25))
                if summary in seenStates:
                    oldRocksFallen, oldTop = seenStates[summary]

                    deltaTop = top - oldTop
                    deltaRocksFallen = rocksFallen - oldRocksFallen

                    # how many times can we repeat this cycle without overshooting sim length?
                    numRepeat = (SIMULATION_LENGTH - rocksFallen) // deltaRocksFallen

                    # skip numRepeat cycles
                    totalHeight += deltaTop * numRepeat
                    rocksFallen += deltaRocksFallen * numRepeat

                seenStates[summary] = (rocksFallen, top)
                break

        rocksFallen += 1

    assert totalHeight == 1572093023267
    print(f'\n{totalHeight}')


if __name__ == "__main__":
    main()
