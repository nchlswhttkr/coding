import sys

commands = [(l[0], int(l[1:])) for l in sys.stdin.readlines()]
n, e, d, wn, we = 0, 0, 90, 1, 10
for (action, value) in commands:
    if action == 'N':
        wn += value
    if action == 'S':
        wn -= value
    if action == 'E':
        we += value
    if action == 'W':
        we -= value
    if action == 'L':
        d = (d - value + 360) % 360
        for _ in range(0, value // 90):
            wn, we = n + (we - e), e - (wn - n)
    if action == 'R':
        d = (d + value) % 360
        for _ in range(0, value // 90):
            wn, we = n - (we - e), e + (wn - n)
    if action == 'F':
        n_offset, e_offset = wn - n, we - e
        for _ in range(value):
            n, e = n + n_offset, e + e_offset
        wn, we = n + n_offset, e + e_offset
print(abs(n) + abs(e))
