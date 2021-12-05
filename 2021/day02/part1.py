from os import getcwd


def main():
    with open(f"{getcwd()}/2021/day02/input.txt", "r") as file:
        depth = 0
        pos = 0

        for line in file.readlines():
            direction, amount = line.split()

            if direction == "forward":
                pos += int(amount)
            elif direction == "up":
                depth -= int(amount)
            elif direction == "down":
                depth += int(amount)

        print(f"Depth: {depth}")
        print(f"Position: {pos}")
        print(f"Product: {depth * pos}")


if __name__ == "__main__":
    main()
