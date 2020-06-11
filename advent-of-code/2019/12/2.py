import sys
import re
from collections import defaultdict


def sign(n):
    return n // abs(n) if n != 0 else 0


xyz = [re.match(r"<x=(.*), y=(.*), z=(.*)>", l) for l in sys.stdin.readlines()]

moons = [[[int(g) for g in match.groups()], [0, 0, 0]] for match in xyz]
start = [[int(g) for g in match.groups()] for match in xyz]
periods = [0, 0, 0]

step = 1
while 0 in periods:
    if (step % 10000) == 0:
        print(step, periods)

    for m1 in range(len(moons)):
        for m2 in range(m1 + 1, len(moons)):
            # direction of gravity upon m1
            gravity = [0, 0, 0]
            for i in range(3):
                gravity[i] = sign(moons[m2][0][i] - moons[m1][0][i])

            # velocity
            for i in range(3):
                moons[m1][1][i] += gravity[i]
                moons[m2][1][i] -= gravity[i]

    # position
    for m in range(len(moons)):
        for i in range(3):
            moons[m][0][i] += moons[m][1][i]

    # check if each dimension has cycled back
    for i in range(3):
        if periods[i] == 0:
            if [s[i] for s in start] == [m[0][i] for m in moons]:
                if [0] * len(moons) == [m[1][i] for m in moons]:
                    periods[i] = step
    step += 1


def gcd(a, b):
    a, b = abs(a), abs(b)
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    while a % b != 0:
        a, b = b, a % b
    return b


def lcm(factors):
    n1 = factors[0]
    for n2 in factors[1:]:
        n1 = (n1 * n2) // gcd(n1, n2)
    return n1


print(periods)
print(lcm(periods))
print(step)
