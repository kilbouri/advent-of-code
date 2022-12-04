from os.path import dirname


def main():
    fuelTotal = 0
    with open(f"{dirname(__file__)}/input.txt", "r") as input:
        for mass in input:
            newFuel = int(mass) // 3 - 2
            while (newFuel > 0):
                fuelTotal += newFuel
                newFuel = newFuel // 3 - 2

    print(fuelTotal)


if __name__ == "__main__":
    main()
