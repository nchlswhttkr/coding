import sys

parents = {}
for line in sys.stdin.readlines():
    [parent_bag, requirements] = line.rstrip(".\n").split(" bags contain ")
    if requirements == "no other bags":
        continue
    for req in requirements.split(', '):
        num, child_bag = req.split(maxsplit=1)
        c = child_bag.rstrip("s")[:-4]
        if c in parents:
            parents[c].append((int(num), parent_bag))
        else:
            parents[c] = [(int(num), parent_bag)]


ancestors = set()
bags_remaining = ["shiny gold"]
while bags_remaining:
    bag = bags_remaining.pop()
    if bag not in parents:
        continue
    for (_, parent) in parents[bag]:
        bags_remaining.append(parent)
        ancestors.add(parent)

print(len(ancestors))
