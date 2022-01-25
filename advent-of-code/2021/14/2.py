import sys

polymer = sys.stdin.readline().strip()
last_element = polymer[-1]
sys.stdin.readline()
insert = {}
for line in sys.stdin.readlines():
    pair = line.strip().split(" -> ")
    insert[pair[0]] = [pair[0][0] + pair[1], pair[1] + pair[0][1]]

pairs = {}
for i in range(len(polymer) - 1):
    pair = polymer[i:i + 2]
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1

for _ in range(40):
    new_pairs = {}
    for (pair, count) in pairs.items():
        for result in insert[pair]:
            if result in new_pairs:
                new_pairs[result] += count
            else:
                new_pairs[result] = count
    pairs = new_pairs

counts = {}
for (pair, count) in pairs.items():
    if pair[0] in counts:
        counts[pair[0]] += count
    else:
        counts[pair[0]] = count
counts[last_element] += 1

quantities = sorted(counts.values())
print(quantities[-1] - quantities[0])
