import sys

score = 0
penalty = {')': 3, ']': 57, '}': 1197, '>': 25137}
for line in sys.stdin.readlines():
    stack = []
    for c in line.strip():
        if c in '([{<':
            stack.append(c)
        elif c != stack.pop().translate(str.maketrans('([{<', ')]}>')):
            score += penalty[c]
            
print(score)