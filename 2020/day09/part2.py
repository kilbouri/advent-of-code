from os import getcwd


def find(nums: list, ambLen: int):
    for i in range(ambLen, len(nums)):

        target = nums[i]
        sliced = set(nums[i - (ambLen): i])

        for first in sliced:

            second = target - first

            if second in sliced and first != second:
                break

            else:
                continue
        else:
            print(f"Did not have a match: {target}")
            return (target, nums[0: i])


def setFind(nums: list, expectedSum: int):
    print(f"Finding a contiguous set that sums to {expectedSum}...")

    for start in range(0, len(nums)):
        for end in range(len(nums), start, -1):

            sliced = nums[start: end]
            if sum(sliced) == expectedSum:
                minNum = min(sliced)
                maxNum = max(sliced)

                print(f"Match: {sliced}")
                print(f"Code: {minNum + maxNum}")
                return


def main():
    with open(f"{getcwd()}/2020/day09/input.txt", 'r') as file:
        nums = list(map(int, file.readlines()))

    res = find(nums, 25)
    setFind(list(res[1]), res[0])


if __name__ == "__main__":
    main()
