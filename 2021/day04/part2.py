from os.path import dirname
from board import Board


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        data = file.read().split("\n\n")

    # create a list of boards from the input
    # note that the first line of data is the sequence of
    # numbers that will be called
    boards = []
    for b in data[1:]:
        boards.append(Board(b))

    completedBoards = []
    for numToCall in map(int, data[0].split(",")):
        # iterate over a copy of the boards so we can maintain
        # safe mutability of the original list
        for board in boards.copy():
            board.markNumber(numToCall)

            # when a board is complete, "move" it from the original
            # list to the complete list
            if board.isComplete():
                boards.remove(board)
                completedBoards.append(board)

                # if moving this board has caused the original list
                # to be empty, we're finished. Output score of last.
                if len(boards) == 0:
                    last = completedBoards[-1]
                    sumOfUnmarked = sum(last.getUnmarkedValues())
                    print(f"Score: {numToCall * sumOfUnmarked}")


if __name__ == "__main__":
    main()
