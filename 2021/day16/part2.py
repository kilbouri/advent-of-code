from functools import reduce
from operator import mul
from os.path import dirname


def getVersionType(bits, i):
    version = int(bits[i:i+3], 2)
    type = int(bits[i+3:i+6], 2)
    return version, type, i+6


def readInt(bits, i, n):
    return int(bits[i:i+n], 2), i + n


def parsePacket(bits, i):
    _, packType, i = getVersionType(bits, i)

    # literal packet
    if packType == 4:
        x = 1
        subVals = []
        while x:
            x, i = int(bits[i]), i + 1
            subVal, i = readInt(bits, i, 4)
            subVals.append(subVal)
        value = reduce(lambda l, n: l*16 + n, subVals)

    # operator packet
    else:
        values = []
        mode, i = readInt(bits, i, 1)

        if mode == 0:
            subpacksLen, i = readInt(bits, i, 15)
            startingIndex = i
            while i < startingIndex + subpacksLen:
                value, i = parsePacket(bits, i)
                values.append(value)
        else:
            nSubpacks, i = readInt(bits, i, 11)
            for _ in range(nSubpacks):
                value, i = parsePacket(bits, i)
                values.append(value)

        # the conditionals for packTypes [5,7] are to prevent errors when values
        # is less than 2 elements, even if the packType is in [0, 3]. Stupid Python.
        value = {
            0: sum(values),
            1: reduce(mul, values),
            2: min(values),
            3: max(values),
            5: int(values[0] > values[1]) if len(values) >= 2 else None,
            6: int(values[0] < values[1]) if len(values) >= 2 else None,
            7: int(values[0] == values[1]) if len(values) >= 2 else None
        }[packType]

    return value, i


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        file = file.read().strip()
        asBinary = bin(int(file, 16))[2:]

    print(f"The packet expression evaluates to {parsePacket(asBinary, 0)[0]}")


if __name__ == "__main__":
    main()
