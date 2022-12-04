from os.path import dirname
from board import Board


def callNumber(numToCall: int, boards: list[Board]) -> Board | None:
    for board in boards:
        board.markNumber(numToCall)

        if board.isComplete():
            return board


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        data = file.read().split("\n\n")

    # create a list of boards
    boards = []
    for b in data[1:]:
        boards.append(Board(b))

    # find the first completed board using the provided sequence of
    # numbers to call
    firstCompleteBoard = None
    for numToCall in map(int, data[0].split(",")):
        firstCompleteBoard = callNumber(numToCall, boards)
        if firstCompleteBoard:
            break

    sumOfUnmarked = sum(firstCompleteBoard.getUnmarkedValues())
    print(f"Score: {numToCall * sumOfUnmarked}")


if __name__ == "__main__":
    main()
