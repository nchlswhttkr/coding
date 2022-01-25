import sys

dots = set()
line = sys.stdin.readline()
while line != "\n":
    coordinates = list(map(int, line.split(',')))
    dots |= {(coordinates[0], coordinates[1])}
    line = sys.stdin.readline()

folds = []
for line in sys.stdin.readlines():
    fold = line.split('=')
    folds.append((fold[0][-1], int(fold[1])))
    
height, width = 0, 0
for fold in folds:
    orientation, position = fold
    if orientation == 'x':
        width = position
    else:
        height = position
    for dot in list(dots):
        x, y = dot
        if orientation == 'x' and x > position:
            dots ^= {(x, y)}
            dots |= {(2 * position - x, y)}
        elif orientation == 'y' and y > position:
            dots ^= {(x, y)}
            dots |= {(x, 2 * position - y)}

for y in range(height):
    for x in range(width):
        print('#' if (x, y) in dots else ' ', end="")
    print()