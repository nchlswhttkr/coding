import sys


def interpret_args(ops, p, n):
    values = [0] * n
    for i in range(n):
        if ops[p] // 10 ** (2 + i) % 10 == 0:
            values[i] = ops[p + i + 1]
        else:
            values[i] = p + i + 1
    return values


ops = [int(i) for i in sys.stdin.readline().split(',')]

p = 0
while ops[p] != 99:
    if ops[p] % 100 == 1:
        args = interpret_args(ops, p, 3)
        ops[args[2]] = ops[args[0]] + ops[args[1]]
        p += 4
    elif ops[p] % 100 == 2:
        args = interpret_args(ops, p, 3)
        ops[args[2]] = ops[args[0]] * ops[args[1]]
        p += 4
    elif ops[p] % 100 == 3:
        args = interpret_args(ops, p, 1)
        ops[args[0]] = int(input())
        p += 2
    elif ops[p] % 100 == 4:
        args = interpret_args(ops, p, 1)
        print(ops[args[0]])
        p += 2
