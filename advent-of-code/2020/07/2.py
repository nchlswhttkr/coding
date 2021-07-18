import sys

children = {}
for line in sys.stdin.readlines():
    [parent_bag, requirements] = line.rstrip(".\n").split(" bags contain ")
    if requirements == "no other bags":
        continue
    children[parent_bag] = []
    for req in requirements.split(', '):
        num, child_bag = req.split(maxsplit=1)
        children[parent_bag].append((int(num), child_bag.rstrip("s")[:-4]))


count = 0
bags_remaining = [(1, "shiny gold")]
while bags_remaining:
    (num, bag) = bags_remaining.pop()
    print(num, bag)
    if bag not in children:
        count += num
    else:
        count += num
        for (factor, child) in children[bag]:
            bags_remaining.append((num * factor, child))

print(count - 1)
