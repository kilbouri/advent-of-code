from os.path import dirname
from pprint import pprint as print


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        instructions = file.read().strip()

    floor = 0
    for index, floorChange in enumerate((1 if char == '(' else -1 for char in instructions)):
        floor += floorChange
        if floor == -1:
            print(index + 1)
            break

    else:
        print('Santa never enters the basement')


if __name__ == "__main__":
    main()
