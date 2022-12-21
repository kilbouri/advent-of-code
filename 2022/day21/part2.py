from os.path import dirname

import re
import z3


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    HUMAN = 'humn'
    monkeys = list(map(lambda x: x.split(': '), lines))

    solver = z3.Solver()

    # Weirdly, trying to solve this using z3.Int will actually fail - something about how it handles
    # division and multiplication of integers, I suppose.
    monkeyValues = {id: z3.Real(id) for id, _ in monkeys}

    for monkeyId, expression in monkeys:
        if monkeyId == HUMAN:
            continue

        if re.match(r'-?\d+', expression):
            # this is an int
            solver.add(monkeyValues[monkeyId] == int(expression))
        else:
            left, op, right = expression.split()

            if monkeyId == 'root':
                solver.add(monkeyValues[left] == monkeyValues[right])
            else:
                expression = {
                    '+': monkeyValues[left] + monkeyValues[right],
                    '-': monkeyValues[left] - monkeyValues[right],
                    '*': monkeyValues[left] * monkeyValues[right],
                    '/': monkeyValues[left] / monkeyValues[right]
                }[op]

                solver.add(monkeyValues[monkeyId] == expression)

    assert solver.check() == z3.sat
    model = solver.model()

    print(model[monkeyValues[HUMAN]])


if __name__ == "__main__":
    main()
