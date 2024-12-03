import sys

def is_safe(levels):
    for i in range(len(levels) - 1):
        if not 1 <= abs(levels[i] - levels[i + 1]) <= 3:
            return False

    return levels == sorted(levels) or levels == sorted(levels, reverse=True)

safe = 0
for line in sys.stdin.readlines():
    levels = [int(i) for i in line.split()]
    for i in range(len(levels)):
        dampened = levels[:i] + levels[i + 1:]
        if is_safe(dampened):
            safe += 1
            break

print(safe)