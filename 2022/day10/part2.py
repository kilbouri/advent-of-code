from os.path import dirname
from termcolor import colored


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    instructions = [line.split(' ') for line in lines]

    screen = [['?' for _ in range(40)] for _ in range(6)]
    clock = 0
    xRegister = 1

    def handleClockTick():
        screenY = (clock - 1) // 40  # the -1 is cuz lists are 0-indexed but our clock is 1-indexed
        screenX = (clock - 1) % 40

        spriteIsVisible = abs(xRegister - screenX) <= 1
        screen[screenY][screenX] = '█' if spriteIsVisible else ' '

    for instruction in instructions:
        if instruction[0] == 'noop':
            # noop does nothing but still ticks the clock 1
            clock += 1
            handleClockTick()  # start and end noop

        else:  # the only other possible op in the input is 'addx'
            clock += 1
            handleClockTick()
            # start addx

            clock += 1
            handleClockTick()
            xRegister += int(instruction[1])  # finish addx

    crtImage = '\n'.join([''.join(line) for line in screen])
    print(''.join([
        colored('The CRT springs to life. It shows this image:\n\n', 'grey'),
        colored(crtImage, 'yellow')
    ]))


if __name__ == "__main__":
    main()
