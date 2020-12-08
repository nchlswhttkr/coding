import sys

rows = [l.strip() for l in sys.stdin.readlines()]
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
total_trees = []
for slope in slopes:
    trees = 0
    position = (0, 0)
    while position[1] < len(rows):
        (col, row) = position
        if rows[row][col] == '#':
            trees += 1
        position = ((col + slope[0]) % len(rows[0]), row + slope[1])
    total_trees.append(trees)

product = 1
for n in total_trees:
    product *= n
print(product)
