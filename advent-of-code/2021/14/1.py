import sys

polymer = list(sys.stdin.readline().strip())
sys.stdin.readline()
insert = {}
for line in sys.stdin.readlines():
    pair = line.strip().split(" -> ")
    insert[pair[0]] = pair[1]

for _ in range(10):
    i = 1
    while i < len(polymer):
        polymer.insert(i, insert[polymer[i - 1] + polymer[i]])
        i += 2

count = {}
for c in polymer:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

quantities = sorted(count.values())
print(quantities[-1] - quantities[0])
