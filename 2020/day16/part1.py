from os import getcwd
from ticket import Ticket
import re


def strToIntSequence(tickStr: str):
    return map(int, tickStr.split(","))


def main():
    # open the file, split into blocks: <fields>, <your ticket>, <other tickets>
    with open(f"{getcwd()}/2020/day16/input.txt") as file:
        file = file.read().strip().split("\n\n")

    validTicket = Ticket()

    # fill the ticket with all the fields and ranges in the input
    allFields = re.findall(r"(.*): (\d+-\d+) or (\d+-\d+)", file[0])
    for field in allFields:
        validTicket.addFieldRange(field[0], [field[1], field[2]])

    # sum the invalid values
    total = 0
    for ticket in list(file[2].splitlines())[1:]:
        for value in strToIntSequence(ticket):
            if not validTicket.isValidValue(value):
                total += value

    print(f"Scanning error rate: {total}")


if __name__ == "__main__":
    main()
