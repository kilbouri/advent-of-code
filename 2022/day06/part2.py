from os.path import dirname
from pprint import pprint as print


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        buffer = file.read().strip()

    WINDOW_SIZE = 14

    for i in range(len(buffer)):
        if len(set(buffer[i:i+WINDOW_SIZE])) == WINDOW_SIZE:
            print(i + WINDOW_SIZE)
            break


if __name__ == "__main__":
    main()
