class Board:

    def __init__(self, board: str) -> None:
        self._board = []
        self._values = set()
        self.markedValues = set()

        for line in board.splitlines():
            nums = line.strip().split(" ")

            row = []
            for num in nums:
                if num:
                    num = int(num)
                else:
                    continue

                self._values.add(num)
                row.append((num, False))

            self._board.append(row)

    def markNumber(self, num: int):
        if num not in self._values:
            return

        self.markedValues.add(num)

        for i in range(len(self._board)):
            try:
                idx = list(self._board[i]).index((num, False))
            except ValueError:
                continue

            self._board[i][idx] = (num, True)
            return

    def isComplete(self):
        for row in self._board:
            valid = True
            for num in row:
                valid = valid and num[1]
            if valid:
                return True

        for i in range(len(self._board[0])):
            valid = True
            for row in self._board:
                valid = valid and row[i][1]
            if valid:
                return True

        return False

    def getUnmarkedValues(self):
        return self._values - self.markedValues
