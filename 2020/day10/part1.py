from os import getcwd


def main():
    with open(f"{getcwd()}/2020/day10/input.txt", "r") as file:
        adapters = list(map(int, file.read().split('\n')))

    adapters.sort()

    dif1 = 0
    dif3 = 1  # include the laptop joltage being 3 more than max

    lastAdapter = 0
    for adapter in adapters:
        dif = adapter - lastAdapter
        lastAdapter = adapter

        if dif == 1:
            dif1 += 1
        elif dif == 3:
            dif3 += 1

    print(f"dif1: {dif1} dif3: {dif3} result: {dif1 * dif3}")


if __name__ == "__main__":
    main()
