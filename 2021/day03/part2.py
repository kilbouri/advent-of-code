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


def findRating(nums: list, useLeastSigBit=False):
    clone = nums.copy()

    for i in range(len(nums[0])):
        filterVal = mostFrequentBit(clone, i)

        if useLeastSigBit:
            filterVal = 1 - filterVal

        clone = filter(lambda x: x[i] == f"{filterVal}", clone)
        clone = list(clone)

        if len(clone) == 1:
            return clone[0]


def main():
    with open(f"{getcwd()}/2021/day03/input.txt", "r") as file:
        data = list(map(str.strip, file.readlines()))

    oxygen = int(findRating(data, False), 2)
    scrubber = int(findRating(data, True), 2)

    print(f"Oxygen: {oxygen}  Scrubber: {scrubber}")
    print(f"Product: {oxygen * scrubber}")


if __name__ == "__main__":
    main()
