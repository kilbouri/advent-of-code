from os.path import dirname


def doDay(fish: list):
    toAppend = []
    for i, f in enumerate(fish):
        if f == 0:
            fish[i] = 6
            toAppend.append(8)
        else:
            fish[i] -= 1

    fish.extend(toAppend)


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        fish = list(map(int, file.read().split(",")))

    for day in range(80):
        doDay(fish)

    print(len(fish))


if __name__ == "__main__":
    main()
