import sys


def in_bounds(seats, i, j):
    return 0 <= i < len(seats) and 0 <= j < len(seats[0])


def occupied(seats, i, j, row_offset, column_offset):
    i, j = i + row_offset, j + column_offset
    if not in_bounds(seats, i, j):
        return False
    while in_bounds(seats, i, j) and seats[i][j] == ".":
        i, j = i + row_offset, j + column_offset
    return in_bounds(seats, i, j) and seats[i][j] == '#'


def determine_status(current, adjacent):
    if current == "L" and adjacent == 0:
        return "#"
    if current == "#" and adjacent >= 5:
        return "L"
    return current


seats = [list(l.strip()) for l in sys.stdin.readlines()]
previous, current = -1, 0
while previous != current:
    adjacent = [[0] * len(seats[0]) for _ in seats]
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            adjacent[i][j] += 1 if occupied(seats, i, j, -1, -1) else 0
            adjacent[i][j] += 1 if occupied(seats, i, j, -1, 0) else 0
            adjacent[i][j] += 1 if occupied(seats, i, j, -1, 1) else 0
            adjacent[i][j] += 1 if occupied(seats, i, j, 0, -1) else 0
            adjacent[i][j] += 1 if occupied(seats, i, j, 0, 1) else 0
            adjacent[i][j] += 1 if occupied(seats, i, j, 1, -1) else 0
            adjacent[i][j] += 1 if occupied(seats, i, j, 1, 0) else 0
            adjacent[i][j] += 1 if occupied(seats, i, j, 1, 1) else 0
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            seats[i][j] = determine_status(seats[i][j], adjacent[i][j])
    previous = current
    current = sum([s.count('#') for s in seats])
    print(current)
print(current)
