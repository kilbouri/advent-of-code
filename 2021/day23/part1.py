from os.path import dirname


def parseRoomLayout(layout: str):
    lines = layout.splitlines()
    hall = lines[1][1:-1]

    roomA = list((lines[3][3], lines[2][3]))
    roomB = list((lines[3][5], lines[2][5]))
    roomC = list((lines[3][7], lines[2][7]))

    return hall, roomA, roomB, roomC


def moveCost(numSpaces, type):
    return {'A': 1, 'B': 10, 'C': 100, 'D': 1000}[type] * numSpaces


def main():
    with open(f"{dirname(__file__)}/test.txt") as file:
        file = file.read()

    roomLayout = parseRoomLayout(file)


if __name__ == "__main__":
    main()
