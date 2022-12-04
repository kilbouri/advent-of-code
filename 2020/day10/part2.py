from os.path import dirname


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        adapters = list(map(int, file.read().split("\n")))

    # add the plug (joltage of 0) and laptop charge
    # port (joltage of max adapter + 3)
    adapters.append(max(adapters) + 3)
    adapters.append(0)

    adapters.sort()

    # "ways" keeps track of the number of valid mutations for chains of
    # length less or equal to the index.
    ways = [0 for i in adapters]
    ways[0] = 1  # there is a single way for 0 adapters
    for i in range(1, len(adapters)):
        # iterates over the list from i to 0, finding the
        # adapters that add no extra joltage to the chain
        for j in range(i, -1, -1):
            if adapters[i] - adapters[j] <= 3:
                # since this adapter doesn't add anything to this chain,
                # it also doesn't add anything to any of the previous ones
                ways[i] += ways[j]

    print(max(ways))


if __name__ == "__main__":
    main()
