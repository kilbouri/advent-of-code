from os.path import dirname
from itertools import permutations

sortedEnc = ["abcefg", "cf", "acdeg", "acdfg", "bcdf",
             "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]


def isValidMapping(ls: str, mapping: dict):
    # using the provided mapping, try to convert each
    # of the 10 numbers on this line to the sorted encoding
    inRemapped = {
        "".join(sorted(map(mapping.get, val)))
        for val in ls.split(" ")
    }

    # the mapping is valid iff it maps all 10 numbers
    # to the same strings in the sorted encoding
    return inRemapped == set(sortedEnc)


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        file = file.readlines()

    total = 0

    for line in file:
        ls = line.strip().split(" | ")[0]
        rs = line.strip().split(" | ")[1]

        for perm in permutations("abcdefg"):
            # m is a mapping from this line's encoding to a sorted
            # seven segment display encoding
            m = {i: j for i, j in zip(perm, "abcdefg")}

            if isValidMapping(ls, m):
                # map the encoding of right-side numbers to sorted
                # seven segment display encoding
                rs = [
                    "".join(sorted(map(m.get, val)))
                    for val in rs.split(" ")
                ]

                # now convert the right hand side to decimal
                actualVal = "".join(
                    str(sortedEnc.index(mapped))
                    for mapped in rs
                )

                total += int(actualVal)
                break  # this permutation worked, lets stop crunching them

    print(f"Sum: {total}")


if __name__ == "__main__":
    main()
