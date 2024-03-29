from os.path import dirname


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        file = [line.strip() for line in file.readlines()]

    opening = '([{<'
    closing = ')]}>'

    scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0

    for line in file:
        stack = list()
        for c in line:
            if c in opening:
                stack.append(c)
            elif c in closing:
                idx = opening.index(stack.pop())
                if c != closing[idx]:
                    score += scoring[c]
                    break  # corrupt line

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
