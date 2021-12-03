from os import getcwd


def main():
    with open(f"{getcwd()}/2020/day03/input.txt", "r") as file:
        lineWidth = 30  # the max position allowed to be accessed in the string array
        horizPos = 0  # the position we're at horizontally

        treeCount = 0
        for line in file:

            if horizPos > lineWidth:
                horizPos -= (lineWidth + 1)

            if line[horizPos] == '#':
                treeCount += 1

            horizPos += 3

        print(f"There were {treeCount} trees.")


if __name__ == "__main__":
    main()
