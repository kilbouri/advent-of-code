from os import getcwd


def dictPlusEq(addTo: dict, key, val, default=0):
    "Performs addTo[key] += val, but does not throw KeyErrors"
    addTo[key] = addTo.get(key, default) + val


def doDay(fish: dict) -> dict:
    "Returns the fish population (a dictionary) after a day"
    newFish = dict()
    for age in fish:
        count = fish[age]
        if age == 0:
            dictPlusEq(newFish, 6, count)
            dictPlusEq(newFish, 8, count)
        else:
            dictPlusEq(newFish, age - 1, count)

    return newFish


def simulateFish(initialFish: iter, days: int) -> int:
    "Simulates days days of life on the initialFish population"
    fishPop = dict()
    for fish in initialFish:
        dictPlusEq(fishPop, fish, 1)

    for _ in range(days):
        fishPop = doDay(fishPop)

    return sum([fishPop[age] for age in fishPop])


def main():
    with open(f"{getcwd()}/2021/day06/input.txt") as file:
        fish = map(int, file.read().split(","))

    print(simulateFish(fish, 256))


if __name__ == "__main__":
    main()
