import sys
import copy
import itertools


def interpret_args(ops, p, n):
    values = [0] * n
    for i in range(n):
        if ops[p] // 10 ** (2 + i) % 10 == 0:
            values[i] = ops[p + i + 1]
        else:
            values[i] = p + i + 1
    return values


def run_program(ops, inputs):
    result = 0
    inputp = 0
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
            ops[args[0]] = inputs[inputp]
            inputp += 1
            p += 2
        elif ops[p] % 100 == 4:
            args = interpret_args(ops, p, 1)
            result = ops[args[0]]
            p += 2
        elif ops[p] % 100 == 5:
            args = interpret_args(ops, p, 2)
            if ops[args[0]] != 0:
                p = ops[args[1]]
            else:
                p += 3
        elif ops[p] % 100 == 6:
            args = interpret_args(ops, p, 2)
            if ops[args[0]] == 0:
                p = ops[args[1]]
            else:
                p += 3
        elif ops[p] % 100 == 7:
            args = interpret_args(ops, p, 3)
            ops[args[2]] = 1 if ops[args[0]] < ops[args[1]] else 0
            p += 4
        elif ops[p] % 100 == 8:
            args = interpret_args(ops, p, 3)
            ops[args[2]] = 1 if ops[args[0]] == ops[args[1]] else 0
            p += 4

    return result


ops = [int(i) for i in sys.stdin.readline().split(',')]

max_signal = 0
for perm in itertools.permutations(range(5)):
    signal = 0
    programs = [copy.deepcopy(ops) for _ in range(len(perm))]

    for i in perm:

        args = [perm[i], signal]
        signal = run_program(programs[i], args)

    max_signal = max(signal, max_signal)

print(max_signal)
