from os import getcwd
from itertools import count
from copy import deepcopy


def step(layout):
    totalMoved = 0

    newLayout = deepcopy(layout)

    south = list()  # optimization!
    for y in range(len(layout)):
        for x in range(len(layout[0])):
            if layout[y][x] == '>':
                newX = (x+1) % len(layout[0])
                if layout[y][newX] == '.':
                    newLayout[y][x] = '.'
                    newLayout[y][newX] = '>'
                    totalMoved += 1
            elif layout[y][x] == 'v':
                south.append((x, y))

    layout = newLayout
    newLayout = deepcopy(layout)
    for x, y in south:
        newY = (y+1) % len(layout)
        if layout[newY][x] == '.':
            newLayout[y][x] = '.'
            newLayout[newY][x] = 'v'
            totalMoved += 1

    return newLayout, totalMoved


def main():
    with open(f"{getcwd()}/2021/day25/input.txt") as file:
        file = file.readlines()

    # file = ['..........\n',
    #         '.>v....v..\n',
    #         '.......>..\n',
    #         '..........\n'
    #         ]

    # file = [
    #     '...>...\n',
    #     '.......\n',
    #     '......>\n',
    #     'v.....>\n',
    #     '......>\n',
    #     '.......\n',
    #     '..vvv..\n'
    # ]

    # file = ["...>>>>>..."]

    layout = [list(line[:-1]) for line in file]
    for i in count(1):
        layout, moved = step(layout)
        if moved == 0:
            print(i)
            break


if __name__ == "__main__":
    main()
