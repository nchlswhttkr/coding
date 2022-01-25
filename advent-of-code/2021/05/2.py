import re, sys

vents = []
grid = {}
for line in sys.stdin.readlines():
    match = re.match(r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)", line)
    x1, y1, x2, y2 = int(match[1]), int(match[2]), int(match[3]), int(match[4])
    for _ in range(max(abs(x1 - x2), abs(y1 - y2)) + 1):
        if (x1, y1) in grid:
            grid[(x1, y1)] += 1
        else:
            grid[(x1, y1)] = 1
        if x1 != x2:
            x1 += 1 if x1 < x2 else -1
        if y1 != y2:
            y1 += 1 if y1 < y2 else -1

print(len(grid) - list(grid.values()).count(1))
