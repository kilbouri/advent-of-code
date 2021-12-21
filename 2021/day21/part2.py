from os import getcwd
from itertools import product
from functools import cache


@cache
def game(p1, p2, turn):
    # score check
    if p1[1] >= 21:
        return 1, 0  # p1 wins 1, p2 wins 0
    if p2[1] >= 21:
        return 0, 1  # p1 wins 0, p2 wins 1

    def move(op, by): return (op + by - 1) % 10 + 1

    if turn:
        dieRolls = product(range(1, 4), repeat=3)

        newPos = [move(p1[0], sum(rolls)) for rolls in dieRolls]
        results = [game((np, p1[1] + np), p2, False) for np in newPos]
    else:
        dieRolls = product(range(1, 4), repeat=3)

        newPos = [move(p2[0], sum(rolls)) for rolls in dieRolls]
        results = [game(p1, (np, p2[1] + np), True) for np in newPos]

    p1Wins = sum(res[0] for res in results)
    p2Wins = sum(res[1] for res in results)

    return p1Wins, p2Wins


def main():
    with open(f"{getcwd()}/2021/day21/input.txt") as file:
        file = file.readlines()
        positions = list(map(lambda line: int(line[28:]), file))

    players = tuple(zip(positions, (0, 0)))
    finalResult = game(*players, True)

    print(f"The overall winner won in {max(finalResult)} universes")


if __name__ == "__main__":
    main()
