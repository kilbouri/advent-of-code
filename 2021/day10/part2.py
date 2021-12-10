from os import getcwd
from functools import reduce


def main():
    with open(f"{getcwd()}/2021/day10/input.txt") as file:
        file = [line.strip() for line in file.readlines()]

    opening = '([{<'
    closing = ')]}>'
    scores = list()

    for line in file:
        stack = list()
        for c in line:
            if c in opening:
                stack.append(c)
            elif c in closing:
                idx = opening.index(stack.pop())
                if c != closing[idx]:
                    break  # corrupt line
        else:
            # incomplete line, find the score
            toComplete = stack[::-1]
            score = reduce(
                lambda lst, nxt: lst * 5 + (opening.index(nxt) + 1), [0] + toComplete)
            scores.append(score)

    scores = sorted(scores)
    print(f"Middle score: {scores[len(scores) // 2]}")


if __name__ == "__main__":
    main()
