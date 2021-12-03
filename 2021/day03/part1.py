from os import getcwd


def mostFrequentBit(nums: list, pos: int):
    zeros = 0
    ones = 0

    for num in nums:
        if num[pos] == '0':
            zeros += 1
        elif num[pos] == '1':
            ones += 1

    # return 1 in the case of tie
    if zeros > ones:
        return 0
    else:
        return 1


def main():
    with open(f"{getcwd()}/2021/day03/input.txt", "r") as file:
        data = list(map(str.strip, file.readlines()))

    lineLen = len(data[0])
    gamma = ""
    epsilon = ""

    for i in range(lineLen):
        mfb = mostFrequentBit(data, i)
        gamma += str(mfb)
        epsilon += str(1-mfb)

    epsilon = int(epsilon, 2)
    gamma = int(gamma, 2)

    print(f"Epsilon: {epsilon}  Gamma: {gamma}")
    print(f"Product: {epsilon * gamma}")


if __name__ == "__main__":
    main()
