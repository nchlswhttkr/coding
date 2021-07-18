import sys

yes_count = 0
group = {}
group_members = 0
for line in map(str.strip, sys.stdin.readlines()):
    if line == "":
        yes_count += list(group.values()).count(group_members)
        group.clear()
        group_members = 0
    else:
        group_members += 1
        for c in line:
            group[c] = group[c] + 1 if c in group else 1
yes_count += list(group.values()).count(group_members)
print(yes_count)
