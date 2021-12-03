from os import curdir


def window(iterable, size=2, incPartials=False):
    """
    Generator yielding a series of sliding windows of 
    specified size (def. 2) over the given iterable
    """
    i = iter(iterable)
    win = []

    for e in range(0, size):
        win.append(next(i))
        if incPartials:
            yield win

    if not incPartials:
        yield win

    for e in i:
        win = win[1:] + [e]
        yield win

    if incPartials:
        for i in range(1, size):
            yield win[i:]


def main():
    with open(curdir + "/2021/day01/input.txt", "r") as file:
        depths = list(map(int, file.readlines()))

        count = -1
        prevWinSum = 0

        for win in window(depths, 3):
            winSum = sum(win)
            if winSum > prevWinSum:
                count += 1
            prevWinSum = winSum

        print(count)  # 1190


if __name__ == "__main__":
    main()
