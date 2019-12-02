import sys

ops = [int(i) for i in sys.stdin.readline().split(',')]
ops[1] = 12
ops[2] = 2
p = 0

while ops[p] != 99:
    if ops[p] == 1:
        ops[ops[p + 3]] = ops[ops[p + 1]] + ops[ops[p + 2]]
    # note the elif, we don't to run this if ops[p] was changed to 2!
    elif ops[p] == 2:
        ops[ops[p + 3]] = ops[ops[p + 1]] * ops[ops[p + 2]]
    p += 4

print(ops[0])
