import sys

left, right = [], []
for line in sys.stdin.readlines():
    split = line.split()
    left.append(int(split[0]))
    right.append(int(split[1]))

diff = 0
for i in range(len(left)):
    diff += abs(sorted(left)[i] - sorted(right)[i])

print(diff)