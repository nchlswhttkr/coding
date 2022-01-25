import sys


scores = []
valid = []
for line in sys.stdin.readlines():
    stack = []
    corrupt = False
    for c in line.strip():
        if corrupt:
            continue
        if c in '([{<':
            stack.append(c)
        elif c != stack.pop().translate(str.maketrans('([{<', ')]}>')):
            corrupt = True
    if not corrupt:
        valid.append(stack)

penalty = {'(': 1, '[': 2, '{': 3, '<': 4}
for stack in valid:
    score = 0
    while len(stack) > 0:
        c = stack.pop()
        score = 5 * score + penalty[c]
    scores.append(score)
            
print(sorted(scores)[len(scores) // 2])