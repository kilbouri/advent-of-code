from os.path import dirname


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as input:
        instructions = input.read().split(",")

    for i in range(0, len(instructions), 4):
        opcode = int(instructions[i])

        if (opcode == 99):
            break
        elif (opcode == 1):
            pos1 = int(instructions[i + 1])
            pos2 = int(instructions[i + 2])
            pos3 = int(instructions[i + 3])
            sum = int(instructions[pos1]) + int(instructions[pos2])
            instructions[pos3] = str(sum)
        elif (opcode == 2):
            pos1 = int(instructions[i + 1])
            pos2 = int(instructions[i + 2])
            pos3 = int(instructions[i + 3])
            product = int(instructions[pos1]) * int(instructions[pos2])
            instructions[pos3] = str(product)

    print("Pos 0: " + str(instructions[0]))


if __name__ == "__main__":
    main()
