from os.path import dirname


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
        screen[screenY][screenX] = '#' if spriteIsVisible else ' '

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

    print('\n'.join([''.join(line) for line in screen]))


if __name__ == "__main__":
    main()
