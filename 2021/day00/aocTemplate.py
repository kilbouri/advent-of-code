from os.path import dirname


def main():
    with open(f"{dirname(__file__)}/test.txt") as file:
        file = file.readlines()
    pass


if __name__ == "__main__":
    main()
