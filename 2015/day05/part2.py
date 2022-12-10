from collections import Counter
from itertools import product
from os.path import dirname
from pprint import pprint as print


def isNice(string: str):
    letterCounts = Counter(string)

    validPatternLetters = [letter for letter, count in letterCounts.items() if count >= 2]
    for pattern in map(''.join, product(validPatternLetters, validPatternLetters)):
        # if there are at least 3 results from splitting on the pattern,
        # we know that the pattern appears twice without overlap
        if len(string.split(pattern)) >= 3:
            # found a valid repeating pattern
            break
    else:
        # loop terminated normally, meaning no repeating pattern found
        return False

    for i in range(2, len(string)):
        substr = string[i - 2:i+1]
        if substr[0] == substr[2]:
            break  # we found a letter that repeats with a single letter in between
    else:
        # loop terminated normally, meaning no letter that repeats with a single letter in between was found
        return False

    return True


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        words = file.read().splitlines()

    niceness = [1 if isNice(word) else 0 for word in words]
    print(sum(niceness))


if __name__ == "__main__":
    main()
