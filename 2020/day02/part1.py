from os import getcwd
import re


def main():
    with open(f"{getcwd()}/2020/day02/input.txt", "r") as file:
        validCount = 0
        for line in file:

            stuffs = re.findall(r'(\d+)-(\d+) (.): (.*)', line)
            res = list(stuffs)

            min, max, character, password = res[0]
            occurences = password.count(character)

            if (occurences in range(int(min), int(max) + 1)):
                validCount += 1

        print("There were " + str(validCount) + " valid passwords in the DB")


if __name__ == "__main__":
    main()
