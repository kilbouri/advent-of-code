from os import getcwd
from pprint import pprint


def main():
    with open(f"{getcwd()}/2021/day08/input.txt") as file:
        file = file.readlines()

    # extract right side values
    patterns = [line.strip().split(" | ")[1] for line in file]

    # count the number of occurences of strings with lengths 2, 3, 4, or 7
    patterns = map(lambda p: sum([
        1 if len(s) in {2, 3, 4, 7} else 0 for s in p.split(" ")
    ]), patterns)

    print(f"Sum: {sum(patterns)}")


if __name__ == "__main__":
    main()
