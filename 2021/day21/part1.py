from os.path import dirname


def diceGen():
    while True:
        for i in range(1, 101):
            yield i


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        file = file.readlines()
        positions = list(map(lambda line: int(line[28:]), file))

    dieVals = diceGen()
    scores = [0] * 2

    numRolls = 0

    p1Moving = True
    while scores[0] < 1000 and scores[1] < 1000:
        moveBy = sum(dieVals.__next__() for _ in range(3))

        if p1Moving:
            positions[0] = (positions[0] + moveBy - 1) % 10 + 1
            scores[0] += positions[0]
            print(
                f"P1 moves {moveBy}, landing on {positions[0]} for score {scores[0]}")
        else:
            positions[1] = (positions[1] - 1 + moveBy) % 10 + 1
            scores[1] += positions[1]
            print(
                f"P2 moves {moveBy}, landing on {positions[1]} for score {scores[1]}")

        p1Moving = not p1Moving
        numRolls += 3

    print(f"Product of loser score and roll count: {min(scores) * numRolls}")


if __name__ == "__main__":
    main()
