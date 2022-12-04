from os.path import dirname


def simulateRound(deckA: list, deckB: list) -> None:
    cardA = deckA.pop(0)
    cardB = deckB.pop(0)

    if int(cardA) > int(cardB):
        # player 1 wins
        deckA.append(cardA)
        deckA.append(cardB)

    elif int(cardA) < int(cardB):
        # player 2 wins
        deckB.append(cardB)
        deckB.append(cardA)


def tallyScore(deck: list) -> int:
    score = 0
    maxMultiplier = len(deck)
    for i, val in enumerate(deck):
        score += (maxMultiplier - i) * int(val)

    return score


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        file = file.read()

    # the winner of each round gets their card, then the opponents card
    # appended to the end of their deck
    myDeck = file.split("\n\n")[0].split("\n")[1:]
    crabsDeck = file.split("\n\n")[1].split("\n")[1:]

    while len(myDeck) * len(crabsDeck) != 0:  # while neither deck has 0 cards:
        simulateRound(myDeck, crabsDeck)

    if len(crabsDeck) == 0:
        print(f"My victorious score is {tallyScore(myDeck)}")
    elif len(myDeck) == 0:
        print(f"The crab\"s victorious score is {tallyScore(crabsDeck)}")


if __name__ == "__main__":
    main()
