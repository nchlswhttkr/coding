import sys


def count_adjacent(seats, adjacent, row_offset, column_offset):
    for i in range(max(0, -row_offset), min(len(seats), len(seats) - row_offset)):
        for j in range(max(0, -column_offset), min(len(seats[0]), len(seats[0]) - column_offset)):
            if seats[i + row_offset][j + column_offset] == '#':
                adjacent[i][j] += 1


def determine_status(current, adjacent):
    if current == "L" and adjacent == 0:
        return "#"
    if current == "#" and adjacent >= 4:
        return "L"
    return current


seats = [list(l.strip()) for l in sys.stdin.readlines()]
previous, current = -1, 0
while previous != current:
    adjacent = [[0] * len(seats[0]) for _ in seats]
    count_adjacent(seats, adjacent, -1, -1)
    count_adjacent(seats, adjacent, -1, 0)
    count_adjacent(seats, adjacent, -1, 1)
    count_adjacent(seats, adjacent, 0, -1)
    count_adjacent(seats, adjacent, 0, 1)
    count_adjacent(seats, adjacent, 1, -1)
    count_adjacent(seats, adjacent, 1, 0)
    count_adjacent(seats, adjacent, 1, 1)
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            seats[i][j] = determine_status(seats[i][j], adjacent[i][j])
    previous = current
    current = sum([s.count('#') for s in seats])
print(current)
