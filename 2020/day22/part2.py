from os import getcwd


def simulateRecursiveCombat(deckA: list, deckB: list) -> int:
    previousConfigurations = []
    while len(deckA) * len(deckB) != 0:
        cardConfiguration = deckA + [" "] + deckB
        if cardConfiguration in previousConfigurations:
            return 1
        else:
            previousConfigurations.append(cardConfiguration)

        cardA = deckA.pop(0)
        cardB = deckB.pop(0)

        # we have to add one to the length to account for the popping
        if len(deckA) < int(cardA) or len(deckB) < int(cardB):
            if int(cardA) > int(cardB):
                deckA.append(cardA)
                deckA.append(cardB)
            else:
                deckB.append(cardB)
                deckB.append(cardA)
            continue

        # start a subgame
        subDeckA = deckA[:int(cardA)]
        subDeckB = deckB[:int(cardB)]

        winner = simulateRecursiveCombat(subDeckA, subDeckB)
        if winner == 1:
            deckA.append(cardA)
            deckA.append(cardB)
        else:
            deckB.append(cardB)
            deckB.append(cardA)

    if len(deckA) == 0:
        return 2
    else:
        return 1


def tallyScore(deck: list) -> int:
    score = 0
    maxMultiplier = len(deck)
    for i, val in enumerate(deck):
        score += (maxMultiplier - i) * int(val)

    return score


def main():
    with open(f"{getcwd()}/2020/day22/input.txt", "r") as file:
        file = file.read()

    myDeck = file.split("\n\n")[0].split("\n")[1:]
    crabsDeck = file.split("\n\n")[1].split("\n")[1:]

    winner = simulateRecursiveCombat(myDeck, crabsDeck)

    if winner == 1:
        print(f"My winning score is {tallyScore(myDeck)}")
    else:
        print(f"The crab\"s winning score is {tallyScore(crabsDeck)}")


if __name__ == "__main__":
    main()
