import sys

def traverse(caves, journey, double):
    if journey[-1] == "end":
        return [journey]

    next_steps = []
    for cave in caves[journey[-1]]:
        if cave != cave.lower():
            for path in traverse(caves, journey[:] + [cave], double):
                next_steps.append(path)
        elif cave in journey:
            if double is None and cave != 'start':
                for path in traverse(caves, journey[:] + [cave], cave):
                    next_steps.append(path)
        else:
            for path in traverse(caves, journey[:] + [cave], double):
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

print(len(traverse(caves, ['start'], None)))