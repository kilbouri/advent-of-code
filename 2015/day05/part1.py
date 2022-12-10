from collections import Counter
from os.path import dirname
from pprint import pprint as print


def isNice(string: str):
    letterCounts = Counter(string)

    if sum(letterCounts[letter] for letter in 'aeiou') < 3:
        # not enough vowels
        return False

    for i in range(1, len(string)):
        substr = string[i-1] + string[i]

        if substr in ['ab', 'cd', 'pq', 'xy']:
            return False  # disallowed substring found

    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            break  # we found a double letter
    else:
        return False  # loop terminated normally, meaning no double letter found

    return True


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        words = file.read().splitlines()

    print(sum([1 if isNice(word) else 0 for word in words]))


if __name__ == "__main__":
    main()
