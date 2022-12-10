from os.path import dirname


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    instructions = [line.split(' ') for line in lines]

    clock = 0
    xRegister = 1
    total = 0  # this is a single value list to get around UnboundLocal errors in handleClockTick

    def handleClockTick():
        nonlocal total
        if clock in [20, 60, 100, 140, 180, 220]:
            total += clock * xRegister

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

    print(total)


if __name__ == "__main__":
    main()
