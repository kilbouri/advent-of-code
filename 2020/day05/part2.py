from math import ceil
from os import getcwd


def main():
    with open(f"{getcwd()}/2020/day05/input.txt", "r") as input:
        lines = input.readlines()

    seats = set()
    for i in lines:
        low = 0
        high = 127
        left = 0
        right = 7
        for j in range(7):
            if i[j] == 'F':
                high = (low+high)//2
            elif i[j] == 'B':
                low = ceil((low+high)/2)
        row = low
        for j in range(7, 10):
            if i[j] == 'L':
                right = (left+right)//2
            elif i[j] == 'R':
                left = ceil((left+right)/2)
        col = left

        seats.add((8 * row) + col)

    for i in range(1000):
        if (int(i + 1) in seats) and (int(i - 1) in seats) and (int(i) not in seats):
            print(i)


if __name__ == "__main__":
    main()
