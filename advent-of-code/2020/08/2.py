import sys


def terminates(instructions, run_before, i, instruction_changed):
    while i < len(instructions):
        ins, arg = instructions[i]
        if i == instruction_changed:
            i += arg if ins == "nop" else 1
        else:
            i += arg if ins == "jmp" else 1
        if i in run_before:
            return False
        run_before.add(i)
    return True


instructions = []
for line in sys.stdin.readlines():
    ins, arg = line.split()
    instructions.append((ins, int(arg)))


run_before = set()
i = 0
acc = 0
instruction_changed = None
while i < len(instructions) and i not in run_before:
    run_before.add(i)
    ins, arg = instructions[i]

    # try different stuff if on nop/jmp
    if (not instruction_changed) and instructions[i][0] != "acc":
        alt_i = i + (arg if ins == "nop" else 1)
        if terminates(instructions, run_before.copy(), alt_i, i):
            instruction_changed = i
            i = alt_i
            continue

    # do normal loop stuff
    if ins == "nop":
        i += 1
    elif ins == "acc":
        i += 1
        acc += arg
    else:
        i += arg

print(acc)
