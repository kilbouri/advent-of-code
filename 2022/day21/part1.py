from os.path import dirname
import re


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    monkeys = {id: expr.replace('/', '//') for id, expr in map(lambda x: x.split(': '), lines)}

    def expandExpr(rootId):
        rawExpr = monkeys[rootId]
        ids = re.findall(r'[a-z]+', rawExpr)

        expanded = rawExpr
        for id in ids:
            expanded = expanded.replace(id, f'({expandExpr(id)})')

        return expanded

    print(eval(expandExpr('root')))


if __name__ == "__main__":
    main()
