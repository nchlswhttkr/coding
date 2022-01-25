import sys

increased = 0
lines = sys.stdin.readlines()
for i in range(1, len(lines)):
    increased += 1 if int(lines[i - 1]) < int(lines[i]) else 0
print(increased)