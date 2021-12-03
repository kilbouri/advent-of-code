from os import getcwd


def main():
    with open(getcwd() + "/2021/dayNN/input.txt", "r") as file:
        print(file.readlines())


if __name__ == "__main__":
    main()
