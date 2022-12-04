from os.path import dirname


def getVersionType(bits, i):
    version = int(bits[i:i+3], 2)
    type = int(bits[i+3:i+6], 2)
    return version, type, i+6


def readInt(bits, i, n):
    return int(bits[i:i+n], 2), i + n


def parsePacket(bits, i):
    version, packType, i = getVersionType(bits, i)
    versionSum = version

    # literal packet
    if packType == 4:
        x = 1
        while x:
            x, i = int(bits[i]), i + 5

    # operator packet
    else:
        mode, i = readInt(bits, i, 1)

        if mode == 0:
            subpacksLen, i = readInt(bits, i, 15)
            startingIndex = i
            while i < startingIndex + subpacksLen:
                subpackVersionSum, i = parsePacket(bits, i)
                versionSum += subpackVersionSum
        else:
            nSubpacks, i = readInt(bits, i, 11)
            for _ in range(nSubpacks):
                subpackVersionSum, i = parsePacket(bits, i)
                versionSum += subpackVersionSum

    return versionSum, i


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        file = file.read().strip()
        asBinary = bin(int(file, 16))[2:]

    print(f"The sum of all version numbers is {parsePacket(asBinary, 0)[0]}")


if __name__ == "__main__":
    main()
