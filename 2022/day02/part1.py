from os.path import dirname
from pprint import pprint as print

ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
TIE = 3
LOSE = 0


def letterToMove(letter):
    match letter:
        case 'X' | 'A': return ROCK
        case 'Y' | 'B': return PAPER
        case _: return SCISSORS


def getOutcome(theirMove, yourMove):
    if theirMove == yourMove:
        return TIE
    if (theirMove, yourMove) in [(ROCK, PAPER), (PAPER, SCISSORS), (SCISSORS, ROCK)]:
        return WIN
    return LOSE


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.readlines()

    turns = [
        (letterToMove(theirMove), letterToMove(myMove))
        for theirMove, myMove in map(str.split, lines)
    ]

    scores = [
        myMove + getOutcome(theirMove, myMove)
        for theirMove, myMove in turns
    ]

    print(sum(scores))


if __name__ == "__main__":
    main()
