import sys

jolts = sorted([int(i) for i in sys.stdin.readlines()])
jolts.insert(0, 0)
jolts.append(jolts[-1] + 3)
arrangements = [1]
for i in range(1, len(jolts)):
    arrangements.append(0)
    for preceeding in range(max(0, i - 3), i):
        if jolts[preceeding] + 3 >= jolts[i]:
            arrangements[i] += arrangements[preceeding]
print(arrangements[-1])
