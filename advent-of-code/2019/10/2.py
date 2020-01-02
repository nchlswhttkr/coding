import sys
import math


def gcd(a, b):
    a, b = abs(a), abs(b)
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    while a % b != 0:
        a, b = b, a % b
    return b


def sign(n):
    return n // abs(n) if n != 0 else 0


def get_angle_from_key(key):
    # must go 0deg -> 360deg, angle from x-y coordinates
    x, y = key
    return - (math.atan2(x, -y) % (2 * math.pi))


grid = [row.rstrip() for row in sys.stdin.readlines()]
HEIGHT = len(grid)
WIDTH = len(grid[0])
asteroids = [{} if c == '#' else None for c in ''.join(grid)]
origin = -1
max_visible = -1

for i in range(len(asteroids)):
    for j in range(i + 1, len(asteroids)):
        if asteroids[i] is not None and asteroids[j] is not None and i != j:
            x1, y1 = i % WIDTH, i // WIDTH
            x2, y2 = j % WIDTH, j // WIDTH

            x_offset = x2 - x1
            y_offset = y2 - y1

            divider = max(gcd(x_offset, y_offset), 1)
            x_step = sign(x_offset) * abs(x_offset) // divider
            y_step = sign(y_offset) * abs(y_offset) // divider

            if (x_step, y_step) in asteroids[i]:
                asteroids[i][(x_step, y_step)].append(j)
            else:
                asteroids[i][(x_step, y_step)] = [j]

            if (-x_step, -y_step) in asteroids[j]:
                asteroids[j][(-x_step, -y_step)].insert(0, i)
            else:
                asteroids[j][(-x_step, -y_step)] = [i]

            if len(asteroids[i]) > max_visible:
                origin = i
                max_visible = len(asteroids[i])


cycle = sorted(asteroids[origin].keys(), key=get_angle_from_key, reverse=True)

lasered = []
c = 0
while len(lasered) < 200:
    if len(asteroids[origin][cycle[c]]) > 0:
        lasered.append(asteroids[origin][cycle[c]][0])
        del asteroids[origin][cycle[c]][0]
    c = (c + 1) % len(cycle)

last = lasered[-1]
print(last % WIDTH * 100 + last // WIDTH)
