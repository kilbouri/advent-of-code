from functools import reduce
from math import lcm
from os.path import dirname

import re


class Monkey:
    def __init__(self, text) -> None:
        pattern = ''.join(r"Monkey \d+:\n"
                          r"  Starting items: ([^\n]*)\n"
                          r"  Operation: ([^\n]*)\n"
                          r"  Test: divisible by (\d+)\n"
                          r"    If true: throw to monkey (\d+)\n"
                          r"    If false: throw to monkey (\d+)")

        # * confused screaming because of the amount of state *
        items, operationString, test, targetTrue, targetFalse = re.match(pattern, text).groups()

        # Parse the captured data
        self.divisor = int(test)
        self.items = [int(x.strip()) for x in items.split(',')]
        self.targets = {True: int(targetTrue), False: int(targetFalse)}
        self.test = lambda worryLevel: worryLevel % self.divisor == 0

        # Use Python's interpreter to avoid having to truly parse the operation.
        # It is slower, sure, but really fast to implement and we are racing. 'nuf said.
        self.inspect = lambda old: eval(operationString[6:], {'old': old})

        # Extra state for problem output
        self.numItemsInspected = 0

    def takeTurn(self, monkeys: list['Monkey'], worryLevelDivisor: int):
        for itemWorryLevel in self.items:
            itemWorryLevel = self.inspect(itemWorryLevel)  # monkey inspects item
            itemWorryLevel %= worryLevelDivisor  # prevent worry level from shooting off to another galaxy

            target = self.targets[self.test(itemWorryLevel)]  # monkey tests where to throw next
            monkeys[target].receiveItem(itemWorryLevel)  # monkey throws item to next monkey

        self.numItemsInspected += len(self.items)
        self.items = []  # we've thrown all the items away

    def receiveItem(self, item: int):
        self.items.append(item)


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        monkeys = [Monkey(chunk) for chunk in file.read().split('\n\n')]

    NUM_ROUNDS = 10_000

    # We want to keep our worry level in check, and each monkey throws based on
    # DIVISIBILITY of our worry level. Therefore, we can keep our worry in check
    # by having each monkey keep track of each item's worry level mod the LCM of
    # all monkeys' divisors (cuz the item may be checked by all monkeys)
    LCM = lcm(*(monkey.divisor for monkey in monkeys))

    for round in range(NUM_ROUNDS):
        if round % 500 == 0:
            print(f'Round {round} of monkey business...')

        for monkey in monkeys:
            monkey.takeTurn(monkeys, LCM)

    monkeyActivity = [monkey.numItemsInspected for monkey in monkeys]
    twoMostActive = tuple(reversed(sorted(monkeyActivity)))[:2]
    score = reduce(lambda a, b: a * b, twoMostActive)

    print(f'After {NUM_ROUNDS} of monkey business, the score is {score}')


if __name__ == "__main__":
    main()
