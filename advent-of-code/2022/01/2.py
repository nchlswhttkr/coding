import sys

calories = [0]
for line in map(lambda x: x.strip(), sys.stdin.readlines()):
    if line == "":
        calories.append(0)
    else:
        calories[-1] += int(line)

print(sum(sorted(calories)[-3:]))
