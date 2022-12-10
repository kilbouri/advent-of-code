from os.path import dirname
from pprint import pprint as print


def main():
    with open(f'{dirname(__file__)}/test.txt', 'r') as file:
        instructions = file.read().strip()

    print(sum([1 if char == '(' else -1 for char in instructions]))


if __name__ == "__main__":
    main()
