import sys


def get_output(initial_ops, noun, verb):
    ops = [i for i in initial_ops]  # lazy way of no mutate
    ops[1] = n
    ops[2] = v
    p = 0

    while ops[p] != 99:
        if ops[p] == 1:
            ops[ops[p + 3]] = ops[ops[p + 1]] + \
                ops[ops[p + 2]]
        # note the elif, we don't to run this if ops[p] was changed to 2!
        elif ops[p] == 2:
            ops[ops[p + 3]] = ops[ops[p + 1]] * \
                ops[ops[p + 2]]
        p += 4

    return ops[0]


TARGET = 19690720
initial_ops = [int(i) for i in sys.stdin.readline().split(',')]
n, v = 0, 0
while get_output(initial_ops, n, v) != TARGET and n + v <= 199:
    if n == 99:
        n = 0
        v += 1
    else:
        n += 1

print(n * 100 + v)
