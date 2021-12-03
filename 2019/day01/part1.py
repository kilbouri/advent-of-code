from os import getcwd


def main():
    sum = 0
    with open(f"{getcwd()}/2019/day01/input.txt", "r") as input:
        for mass in input:
            # first line is 74159 given input 148319
            sum += int(mass) // 3 - 2

    print(sum)


if __name__ == "__main__":
    main()
