import sys

rows = [l.strip() for l in sys.stdin.readlines()]
slope = (3, 1)
trees = 0
position = (0, 0)
while position[1] < len(rows):
    (col, row) = position
    if rows[row][col] == '#':
        trees += 1
    position = ((col + slope[0]) % len(rows[0]), row + slope[1])
print(trees)
