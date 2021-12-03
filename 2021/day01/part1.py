from os import getcwd


def main():
    with open(getcwd() + "/2021/day01/input.txt", "r") as file:
        depths = list(map(int, file.readlines()))

        lastDepth = depths[0]
        depthIncs = 0

        for line in depths:
            if line > lastDepth:
                depthIncs += 1
            lastDepth = line

        print(depthIncs) # 1162


if __name__ == "__main__":
    main()
