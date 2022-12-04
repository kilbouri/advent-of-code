from os.path import dirname
import re


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        validCount = 0
        for line in file:

            stuffs = re.findall(r'(\d+)-(\d+) (.): (.*)', line)
            res = list(stuffs)

            first, last, character, password = res[0]

            letterAppears = 0
            if password[int(first) - 1] == character:
                letterAppears += 1

            if password[int(last) - 1] == character:
                letterAppears += 1

            if (letterAppears == 1):
                validCount += 1

        print("There were " + str(validCount) + " valid passwords in the DB")


if __name__ == "__main__":
    main()
