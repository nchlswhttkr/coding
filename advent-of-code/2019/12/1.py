import sys
import re


def sign(n):
    return n // abs(n) if n != 0 else 0


xyz = [re.match(r"<x=(.*), y=(.*), z=(.*)>", l) for l in sys.stdin.readlines()]

moons = [[[int(g) for g in match.groups()], [0, 0, 0]] for match in xyz]

steps = 1000
for _ in range(steps):
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

print(sum(sum(map(abs, moon[0])) * sum(map(abs, moon[1])) for moon in moons))
