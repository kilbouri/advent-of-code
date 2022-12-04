from os.path import dirname


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as input:
        numbers = set(map(int, map(str.strip, input.readlines())))

        for number in numbers:
            print(number)
            if 2020 - number in numbers:
                product = number * (2020 - number)
                print("Found: " + str(2020 - number) + " * " +
                      str(number) + " = " + str(product))
                break


if __name__ == "__main__":
    main()
