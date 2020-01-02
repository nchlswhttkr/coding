import sys


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


grid = [row.rstrip() for row in sys.stdin.readlines()]
HEIGHT = len(grid)
WIDTH = len(grid[0])
asteroids = [{} if c == '#' else None for c in ''.join(grid)]

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

            asteroids[i][(x_step, y_step)] = True
            asteroids[j][(-x_step, -y_step)] = True

print(max([len(a) if a is not None else 0 for a in asteroids]))
