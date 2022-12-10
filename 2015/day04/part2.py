from hashlib import md5
from itertools import count
from os.path import dirname
from pprint import pprint as print


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        secret = file.read().strip()

    # this one is fairly slow, I recommend using a JIT-capable version of Python
    # such as PyPy: https://www.pypy.org/

    NUM_LEADING_ZEROES = 6

    for i in count():
        digest = md5(f'{secret}{i}'.encode()).hexdigest()
        if digest.startswith('0' * NUM_LEADING_ZEROES):
            print(digest + ' resulted from the nonce ' + str(i))
            break


if __name__ == "__main__":
    main()
