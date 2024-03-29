from os.path import dirname


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        aim = 0
        depth = 0
        pos = 0

        for line in file.readlines():
            direction, amount = line.split()

            if direction == "forward":
                pos += int(amount)
                depth += int(amount) * aim
            elif direction == "up":
                aim -= int(amount)
            elif direction == "down":
                aim += int(amount)

        print(f"Depth: {depth}")
        print(f"Position: {pos}")
        print(f"Product: {depth * pos}")


if __name__ == "__main__":
    main()
