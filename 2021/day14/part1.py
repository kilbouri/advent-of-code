from collections import Counter
from os import getcwd


def doStep(polymer, rules):
    newPolymer = [
        polymer[i-1] + rules.get(polymer[i-1:i+1], '')
        for i in range(1, len(polymer))
    ]
    return "".join(newPolymer) + polymer[-1]


def main():
    with open(f"{getcwd()}/2021/day14/input.txt") as file:
        file = file.read().split("\n\n")

        polymer = file[0].strip()
        instructions = [s.strip().split(' -> ') for s in file[1].splitlines()]

    rules = {i[0]: i[1] for i in instructions}

    for i in range(10):
        polymer = doStep(polymer, rules)

    elements = Counter(polymer).most_common()
    mf = elements[0][1]
    lf = elements[-1][1]

    print(f"After 10 steps, the result is {mf - lf}")


if __name__ == "__main__":
    main()
