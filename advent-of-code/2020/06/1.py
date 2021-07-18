import sys

yes_count = 0
group = set()
for line in map(str.strip, sys.stdin.readlines()):
    if line == "":
        yes_count += len(group)
        group.clear()
    else:
        for c in line:
            group.add(c)
yes_count += len(group)
print(yes_count)
