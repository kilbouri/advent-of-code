from collections import Counter
from os import getcwd


def doStep(oldPairs, rules):
    newPairs = Counter()

    # rule AB -> C dictates that AB becomes (AC, CB), thus
    # n AB pairs becomes n AC pairs and n CB pairs
    for pair in oldPairs:
        newPairs[pair[0] + rules[pair]] += oldPairs[pair]
        newPairs[rules[pair] + pair[1]] += oldPairs[pair]

    return newPairs


def main():
    with open(f"{getcwd()}/2021/day14/input.txt") as file:
        file = file.read().split("\n\n")

        polymer = file[0].strip()

        rules = [s.strip().split(' -> ') for s in file[1].splitlines()]
        rules = {r[0]: r[1] for r in rules}

    # count the initial pairs in the polymer
    polymerPairs = Counter()
    for i in range(1, len(polymer)):
        polymerPairs[polymer[i-1:i+1]] += 1

    # simulate 40 iterations of the insertion rules being applied
    for i in range(40):
        print(f"Step {i}")
        polymerPairs = doStep(polymerPairs, rules)

    # determine the number of occurences of each element
    elementCounts = Counter()
    for pair in polymerPairs:
        # we only count the first: the second will be at the start of
        # another pair later. This prevents double counting.
        elementCounts[pair[0]] += polymerPairs[pair]
    elementCounts[polymer[-1]] += 1

    # get a list of the element counts, in order from most to least frequent
    elementFreqs = elementCounts.most_common()
    mf = elementFreqs[0][1]
    lf = elementFreqs[-1][1]

    print(f"After 40 steps, the result is {mf - lf}")


if __name__ == "__main__":
    main()
