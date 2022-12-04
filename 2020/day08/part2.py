from os.path import dirname
import re


def tryBootCode(bootCode: list):
    cpuCounter = 0
    accumulator = 0
    addressesVisted = list()
    while cpuCounter < len(bootCode):

        op = bootCode[cpuCounter]

        if cpuCounter in addressesVisted:
            return False

        addressesVisted.append(cpuCounter)

        if op[0] == "jmp":
            cpuCounter += int(op[1])
            continue
        elif op[0] == "acc":
            accumulator += int(op[1])

        cpuCounter += 1
    if (cpuCounter == len(bootCode)):
        return accumulator
    else:
        return False


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as input:
        file = input.read()

    operations = re.findall(r"(nop|jmp|acc) (\+\d+|-\d+)", file)
    for i in range(len(operations)):
        opMutation = operations.copy()

        if operations[i][0] == "nop":
            opMutation[i] = ("jmp", operations[i][1])
            worked = tryBootCode(opMutation)

            if worked is not False:
                print(worked)
                return

            else:
                opMutation = operations.copy()

        elif operations[i][0] == "jmp":
            opMutation[i] = ("nop", operations[i][1])
            worked = tryBootCode(opMutation)

            if worked is not False:
                print(worked)
                return
            else:
                opMutation = operations.copy()


if __name__ == "__main__":
    main()
