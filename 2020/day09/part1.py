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
            return


def main():
    with open(f"{getcwd()}/2020/day09/input.txt", 'r') as file:
        nums = list(map(int, file.read().split()))

    find(nums, 25)


if __name__ == "__main__":
    main()
