import sys

jolts = sorted([int(i) for i in sys.stdin.readlines()])
diffs = [0, 0, 0, 0]
current_joltage = 0
for jolt in jolts:
    diffs[jolt - current_joltage] += 1
    current_joltage = jolt
diffs[3] += 1  # inbuilt adapter
print(diffs[1] * diffs[3])
