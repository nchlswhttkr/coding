import sys

commands = [(l[0], int(l[1:])) for l in sys.stdin.readlines()]
n, e, d = 0, 0, 90
for (action, value) in commands:
    if action == 'N':
        n += value
    if action == 'S':
        n -= value
    if action == 'E':
        e += value
    if action == 'W':
        e -= value
    if action == 'L':
        d = (d - value + 360) % 360
    if action == 'R':
        d = (d + value) % 360
    if action == 'F':
        if d == 0:
            n += value
        if d == 180:
            n -= value
        if d == 90:
            e += value
        if d == 270:
            e -= value
print(abs(n) + abs(e))
