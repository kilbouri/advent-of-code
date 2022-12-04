from os.path import dirname
import re


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as input:
        file = input.read()

    operations = re.findall(r"(nop|jmp|acc) (\+\d+|-\d+)", file)

    cpuCounter = 0
    accumulator = 0

    addressesVisted = list()
    while cpuCounter < len(operations):

        op = operations[cpuCounter]
        print(op)

        if cpuCounter in addressesVisted:
            break

        addressesVisted.append(cpuCounter)

        if op[0] == "jmp":
            cpuCounter += int(op[1])
            continue
        elif op[0] == "acc":
            accumulator += int(op[1])

        cpuCounter += 1

    print(accumulator)


if __name__ == "__main__":
    main()
