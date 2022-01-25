import sys

risk_level = 0
cavern = list(map(lambda x: x.strip(), sys.stdin.readlines()))
height, width = len(cavern), len(cavern[0])
depths = [[0] * width for _ in range(height)]
for i in range(height):
    for j in range(width):
        if j < width - 1:
            if cavern[i][j] < cavern[i][j + 1]:
                depths[i][j + 1] += 1
            else:
                depths[i][j] += 1
        if i < height - 1:
            if cavern[i][j] < cavern[i + 1][j]:
                depths[i + 1][j] += 1
            else:
                depths[i][j] += 1
        if depths[i][j] == 0:
            risk_level += int(cavern[i][j]) + 1
print(risk_level)