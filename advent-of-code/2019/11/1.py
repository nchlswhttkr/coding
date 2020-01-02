import sys
from collections import defaultdict
from queue import Queue


def interpret_args(ops, p, n, base):
    values = [0] * n
    for i in range(n):
        mode = ops[p] // 10 ** (2 + i) % 10
        if mode == 0:
            values[i] = ops[p + i + 1]
        elif mode == 2:
            values[i] = base + ops[p + i + 1]
        else:
            values[i] = p + i + 1
    return values


ops = defaultdict(lambda: 0)
i = 0
for instruction in sys.stdin.readline().rstrip().split(','):
    ops[i] = int(instruction)
    i += 1

p = 0
base = 0
x, y, facing = 0, 0, 'U'
out = Queue()
panels = defaultdict(lambda: 0)
while ops[p] != 99:
    if ops[p] % 100 == 1:
        args = interpret_args(ops, p, 3, base)
        ops[args[2]] = ops[args[0]] + ops[args[1]]
        p += 4
    elif ops[p] % 100 == 2:
        args = interpret_args(ops, p, 3, base)
        ops[args[2]] = ops[args[0]] * ops[args[1]]
        p += 4
    elif ops[p] % 100 == 3:
        args = interpret_args(ops, p, 1, base)
        ops[args[0]] = panels[(x, y)]
        p += 2
    elif ops[p] % 100 == 4:
        args = interpret_args(ops, p, 1, base)
        out.put(ops[args[0]])
        p += 2
    elif ops[p] % 100 == 5:
        args = interpret_args(ops, p, 2, base)
        if ops[args[0]] != 0:
            p = ops[args[1]]
        else:
            p += 3
    elif ops[p] % 100 == 6:
        args = interpret_args(ops, p, 2, base)
        if ops[args[0]] == 0:
            p = ops[args[1]]
        else:
            p += 3
    elif ops[p] % 100 == 7:
        args = interpret_args(ops, p, 3, base)
        ops[args[2]] = 1 if ops[args[0]] < ops[args[1]] else 0
        p += 4
    elif ops[p] % 100 == 8:
        args = interpret_args(ops, p, 3, base)
        ops[args[2]] = 1 if ops[args[0]] == ops[args[1]] else 0
        p += 4
    elif ops[p] % 100 == 9:
        args = interpret_args(ops, p, 1, base)
        base += ops[args[0]]
        p += 2

    if out.qsize() >= 2:
        # paint the current square
        color = out.get()
        panels[(x, y)] = color

        # turn left/right and move
        turn = out.get()
        if (facing == 'U' and turn == 0) or (facing == 'D' and turn == 1):
            facing = 'L'
            x, y = x - 1, y
        elif (facing == 'L' and turn == 0) or (facing == 'R' and turn == 1):
            facing = 'D'
            x, y = x, y - 1
        elif (facing == 'D' and turn == 0) or (facing == 'U' and turn == 1):
            facing = 'R'
            x, y = x + 1, y
        elif (facing == 'R' and turn == 0) or (facing == 'L' and turn == 1):
            facing = 'U'
            x, y = x, y + 1

print(len(panels))
