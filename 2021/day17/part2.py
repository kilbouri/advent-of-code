from os.path import dirname
from re import findall
from math import sqrt


def willHitTarget(vx, vy, targetRegion):
    lx, rx, by, ty = targetRegion
    x, y = 0, 0

    def mayStillHit():
        # below the region and moving downwards?
        vCheck = y < by and vy <= 0
        # moving away from the region horizontally?
        hCheck = (x < lx and vx <= 0) or (x > rx and vx >= 0)

        return not (hCheck or vCheck)

    def hitTarget():
        return lx <= x <= rx and by <= y <= ty

    while mayStillHit():
        x += vx
        y += vy

        vx -= 1 if vx > 0 else 0 if vx == 0 else -1
        vy -= 1

        if hitTarget():
            return True

    return False


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        target = tuple(map(int, findall(r"(-?\d+)", file.read())))
        lx, rx, by, _ = target

    validVels = set()

    # Explanation of these "magic formulae":
    # vxMin: any velocity v which does not have v(v+1)/2 >= lx will not reach the target
    # vxMax: any velocity greater than rx will pass the target on the first step
    # vyMin: any velocity less than by will fall under the target on the first step
    # vyMax: since y velocity decreases by a constant each step, the probe will have Y velocity
    #        that is exactly -initialVelocity when it comes back down to y=0.
    #        Also, since we must not overshoot the target on the next step, we are bounded to
    #        abs(by) - 1 as our starting velocity. It will become -abs(by) + 1 when the probe
    #        comes back down to y=0, then -abs(by) on the next step which will always fall *exactly*
    #        on the bounds.

    vxMin = 0.5 * (sqrt(1 + 8 * lx) - 1)  # x = v(v+1)/2 solved for v
    vxMax = rx
    vyMin = by
    vyMax = abs(by) - 1

    for y in range(vyMin, vyMax + 1):
        for x in range(int(vxMin), vxMax + 1):
            if willHitTarget(x, y, target):
                validVels.add((x, y))

    print(f"There are {len(validVels)} velocities that reach the target.")


if __name__ == "__main__":
    main()
