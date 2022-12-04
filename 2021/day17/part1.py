from os.path import dirname
from re import findall


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        target = tuple(map(int, findall(r"(-?\d+)", file.read())))

    # Explanation:
    #     Since y velocity decreases by a constant each step, the probe will have Y velocity
    # that is exactly -initialVelocity when it comes back down to y=0.
    #
    #     Also, since we must not overshoot the target on the next step, we are bounded to
    # abs(by) - 1 as our starting velocity. It will become -abs(by) + 1 when the probe
    # comes back down to y=0, then -abs(by) on the next step which will always fall *exactly*
    # on the bounds.
    #
    #     It follows that if the max velocity in the Y direction is v = abs(by) - 1, then
    # the highest Y we can reach is v(v+1)/2. We do integer division as we can only consider
    # integer values for y

    vyMax = abs(target[2]) - 1
    peak = vyMax * (vyMax + 1) // 2
    print(f"The highest Y value is {peak}.")


if __name__ == "__main__":
    main()
