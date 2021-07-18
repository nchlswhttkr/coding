import sys

instructions = []
for line in sys.stdin.readlines():
    ins, arg = line.split()
    instructions.append((ins, int(arg)))

run_before = set()
i = 0
acc = 0
while i not in run_before:
    run_before.add(i)
    ins, arg = instructions[i]
    if ins == "nop":
        i += 1
    elif ins == "acc":
        i += 1
        acc += arg
    else:
        i += arg

print(acc)
