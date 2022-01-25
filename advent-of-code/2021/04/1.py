import sys

winning_arrangements = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24],
    [0, 5, 10, 15, 20],
    [1, 6, 11, 16, 21],
    [2, 7, 12, 17, 22],
    [3, 8, 13, 18, 23],
    [4, 9, 14, 19, 24],
    # [0, 6, 12, 18, 24],
    # [4, 8, 12, 16, 20],
]

lines = sys.stdin.readlines()
draw = [n.strip() for n in lines[0].split(',')]
boards = []

for i in range(2, len(lines), 6):
    lookup, marks = {}, [False] * 25
    for j in range(5):
        cells = lines[i + j].strip().split()
        lookup[cells[0]] = j * 5
        lookup[cells[1]] = j * 5 + 1
        lookup[cells[2]] = j * 5 + 2
        lookup[cells[3]] = j * 5 + 3
        lookup[cells[4]] = j * 5 + 4
    boards.append((lookup, marks))

score = -1
i = 0
while score < 0:
    call = draw[i]
    for lookup, marks in boards:
        if call in lookup:
            marks[lookup[call]] = True
            for arrangement in winning_arrangements:
                if False not in map(lambda x: marks[x], arrangement):
                    score = int(call) * sum(map(lambda x: int(x[0]) if not marks[x[1]] else 0, lookup.items()))
    i += 1

print(score)