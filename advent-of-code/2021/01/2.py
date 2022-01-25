import sys

increased = 0
lines = [int(line) for line in sys.stdin.readlines()]
for i in range(3, len(lines)):
    increased += 1 if sum(lines[i - 3:i]) < sum(lines[i - 2: i + 1]) else 0
print(increased)