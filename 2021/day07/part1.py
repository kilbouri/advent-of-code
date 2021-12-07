from os import getcwd


def main():
    with open(f"{getcwd()}/2021/day07/input.txt") as file:
        file = list(map(int, file.read().split(",")))

    targetRange = range(min(file), max(file) + 1)
    totalMoveCost = (lambda p: sum([abs(p - pos) for pos in file]))

    costs = [totalMoveCost(target) for target in targetRange]
    print(f"Min fuel: {min(costs)} (at {costs.index(min(costs))})")


if __name__ == "__main__":
    main()
