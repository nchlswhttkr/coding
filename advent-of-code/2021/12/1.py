import sys

def traverse(caves, journey):
    if journey[-1] == "end":
        return [journey]

    next_steps = []
    for cave in caves[journey[-1]]:
        if not (cave == cave.lower() and cave in journey):
            for path in traverse(caves, journey[:] + [cave]):
                next_steps.append(path)
    return next_steps

caves = {}
for line in sys.stdin.readlines():
    c1, c2 = line.strip().split('-')
    if c1 not in caves:
        caves[c1] = [c2]
    else:
        caves[c1].append(c2)
    if c2 not in caves:
        caves[c2] = [c1]
    else:
        caves[c2].append(c1)

count = 0
for path in traverse(caves, ['start']):
    visits_small = False
    for cave in path[1:-1]:
        if not visits_small and cave == cave.lower():
            visits_small = True
    count += 1 if visits_small else 0
print(count)
    