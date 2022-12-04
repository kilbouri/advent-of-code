from os.path import dirname
from ast import literal_eval
from copy import deepcopy


def reduce(sfNum):
    x = deepcopy(sfNum)

    flag = True
    while flag:
        flag = False
        stack = [(0, x, [])]

        # EXPLOSION CHECK
        while stack:
            depth, val, parent = stack.pop()
            if not isinstance(val, list):
                continue

            # explode when 4 levels or deeper
            if depth >= 4:
                for a, ix in parent:
                    if ix > 0:
                        # find leftmost regular number
                        while isinstance(a[ix-1], list):
                            a = a[ix-1]
                            ix = len(a)
                        # add left side of val to it
                        a[ix-1] += val[0]
                        break
                for a, ix in parent:
                    if ix < len(a) - 1:
                        # find rightmost regular number
                        while isinstance(a[ix+1], list):
                            a = a[ix+1]
                            ix = -1
                        # add right side of val to it
                        a[ix+1] += val[1]
                        break
                parent[0][0][parent[0][1]] = 0
                flag = True
                break
            else:
                # push all sublists onto the stack
                for i, sub in list(enumerate(val))[::-1]:
                    stack.append((depth+1, sub, [[val, i]] + parent))
        if flag:
            continue

        # SPLIT CHECK
        stack = [(0, x, None, None)]
        while stack:
            depth, val, parent, index = stack.pop()
            if not isinstance(val, list):
                if val >= 10:
                    parent[index] = [val // 2, (val+1) // 2]
                    flag = True
                    break
            else:
                for i, sub in list(enumerate(val))[::-1]:
                    stack.append((depth + 1, sub, val, i))

    return x


def add(a, b):
    return reduce([a, b])


def magnitude(x):
    if isinstance(x, list):
        return 3 * magnitude(x[0]) + 2 * magnitude(x[1])
    else:
        return x


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        file = file.readlines()
        sfNums = list(map(literal_eval, file))

    maxVal = -1
    for a in sfNums:
        for b in sfNums:
            maxVal = max(maxVal, magnitude(add(a, b)))

    print(maxVal)  # 4490


if __name__ == "__main__":
    main()
