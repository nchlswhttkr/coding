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

for fold in folds[0:1]:
    orientation, position = fold
    for dot in list(dots):
        x, y = dot
        if orientation == 'x' and x > position:
            dots ^= {(x, y)}
            dots |= {(2 * position - x, y)}
        elif orientation == 'y' and y > position:
            dots ^= {(x, y)}
            dots |= {(x, 2 * position - y)}

print(len(dots))