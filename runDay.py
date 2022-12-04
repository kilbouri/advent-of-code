#!/usr/bin/env python3

from os import system, path
from sys import argv


def main():

    try:
        from termcolor import colored
    except ModuleNotFoundError:
        print("termcolor required - 'pip install termcolor' and then run again")
        return

    if len(argv) != 4:
        print("Invalid number of arguments.")
        print("   Usage: ./runDay <year: int> <day: int> <part: int>")
        exit()

    year = argv[1]
    day = argv[2]
    part = argv[3]

    command = f"python3 \"{path.dirname(__file__)}/{year}/day{day.zfill(2)}/part{part}.py\""

    print(colored(f"Launching Advent of Code {year} - Day {day} Part {part}", 'green'))
    print(f"{colored('Executing', 'red')} {colored(command, 'grey')}")

    system(command)


if __name__ == "__main__":
    main()
