import sys

previous_flashes, flashes = 0, 0
step = 0
squids = [list(map(int, list(line.strip()))) for line in sys.stdin.readlines()]
while flashes - previous_flashes != 100:
    stack = []
    for i in range(10):
        for j in range(10):
            squids[i][j] += 1
            if squids[i][j] == 10:
                stack.append((i, j))

    previous_flashes = flashes
    while len(stack) > 0:
        flashes += 1
        i, j = stack.pop()
        for x in range(-1, 2):
            for y in range(-1, 2):
                if 0 <= x + i < 10 and 0 <= j + y < 10:
                    squids[i + x][j + y] += 1
                    if squids[i + x][j + y] == 10:
                        stack.append((i + x, j + y))

    for i in range(10):
        for j in range(10):
            if squids[i][j] >= 10:
                squids[i][j] = 0

    step += 1

print(step)
