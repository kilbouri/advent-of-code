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


def letterToOutcome(letter):
    match letter:
        case 'X' | 'A': return LOSE
        case 'Y' | 'B': return TIE
        case _: return WIN


def getMove(move, desiredOutcome):
    # Conveniently the possible moves are laid out in such a way that 1 loses to 2, 2 loses to 3, and 3 loses to 1.
    # This means to lose, we decrement and underflow to 3.
    # Conversely, to win, we increment and overflow to 1.
    # To tie we obviously just play the same.

    if desiredOutcome == WIN:
        return move % 3 + 1
    if desiredOutcome == LOSE:
        return (move - 2) % 3 + 1

    return move


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    turns = [
        (letterToMove(theirMove), letterToOutcome(myMove))
        for theirMove, myMove in map(str.split, lines)
    ]

    scores = [
        getMove(theirMove, desiredOutcome) + desiredOutcome
        for theirMove, desiredOutcome in turns
    ]

    print(sum(scores))


if __name__ == "__main__":
    main()
