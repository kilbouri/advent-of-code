from os.path import dirname
from timeit import timeit


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    numbers = list(enumerate(map(int, lines)))
    mixed = numbers  # copying not required because we exlcusively use slicing

    for pair in numbers:
        _, value = pair

        origIndex = mixed.index(pair)

        # Rotates numbers to put pair as the first element, while also removing it
        mixed = mixed[origIndex + 1:] + mixed[:origIndex]  # rotate pair to front and pop

        # How far do we need to rotate for this number?
        shift = value % len(mixed)

        # Apply rotation, then append the popped element
        mixed = mixed[shift:] + mixed[:shift] + [pair]

    baseIndex = [mixedIndex for mixedIndex, (_, value) in enumerate(mixed) if value == 0][0]
    coordinates = (mixed[(baseIndex + offset) % len(mixed)][1] for offset in (1000, 2000, 3000))
    print(sum(coordinates))


if __name__ == "__main__":
    print(timeit(main, number=1))
