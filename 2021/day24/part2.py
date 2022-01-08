import z3


def add_constraints(s, inp):
    for digit in inp:
        s.add(digit > 0)
        s.add(digit < 10)

    v4 = (inp[0] + 12) * (inp[0] != 14)
    v6 = (v4 % 26 + 13 != inp[1]) * (inp[1] + 6) + (25 * (v4 % 26 + 13 != inp[1]) + 1) * v4
    v8 = (v6 % 26 + 12 != inp[2]) * (inp[2] + 4) + (25 * (v6 % 26 + 12 != inp[2]) + 1) * v6
    v10 = (v8 % 26 + 14 != inp[3]) * (inp[3] + 5) + (25 * (v8 % 26 + 14 != inp[3]) + 1) * v8
    v12 = inp[4] * (v10 % 26 + 13 != inp[4]) + (25 * (v10 % 26 + 13 != inp[4]) + 1) * v10
    v14 = (inp[5] + 4) * (v12 % 26 - 7 != inp[5]) + v12 / 26 * (25 * (v12 % 26 - 7 != inp[5]) + 1)
    v16 = (v14 % 26 - 13 != inp[6]) * (inp[6] + 15) + (25 * (v14 % 26 - 13 != inp[6]) + 1) * (v14 / 26)
    v18 = (inp[7] + 14) * (v16 % 26 + 10 != inp[7]) + (25 * (v16 % 26 + 10 != inp[7]) + 1) * v16
    v20 = (v18 % 26 - 7 != inp[8]) * (inp[8] + 6) + (25 * (v18 % 26 - 7 != inp[8]) + 1) * (v18 / 26)
    v22 = (inp[9] + 14) * (v20 % 26 + 11 != inp[9]) + (25 * (v20 % 26 + 11 != inp[9]) + 1) * v20
    v24 = (inp[10] + 8) * (v22 % 26 - 9 != inp[10]) + v22 / 26 * (25 * (v22 % 26 - 9 != inp[10]) + 1)
    v26 = (inp[11] + 5) * (v24 % 26 - 2 != inp[11]) + v24 / 26 * (25 * (v24 % 26 - 2 != inp[11]) + 1)
    v28 = (inp[12] + 14) * (v26 % 26 - 9 != inp[12]) + v26 / 26 * (25 * (v26 % 26 - 9 != inp[12]) + 1)
    res = (inp[13] + 4) * (v28 % 26 - 14 != inp[13]) + v28 / 26 * (25 * (v28 % 26 - 14 != inp[13]) + 1)

    tot = 0
    for digit in inp:
        tot = tot * 10 + digit

    s.add(res == 0)
    return tot


def solve(inp, maximize=True):
    s = z3.Optimize()
    value = add_constraints(s, inp)

    if maximize:
        s.maximize(value)
    else:
        s.minimize(value)

    assert s.check() == z3.sat

    m = s.model()
    return m.eval(value)


inp = [z3.Int('x{}'.format(i)) for i in range(14)]

print('Part 2:', solve(inp, maximize=False))
