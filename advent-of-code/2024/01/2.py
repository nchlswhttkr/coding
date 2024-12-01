import sys
import collections

left, right = (), collections.defaultdict(lambda: 0)
for line in sys.stdin.readlines():
    split = line.split()
    left += (int(split[0]),)
    right[int(split[1])] += 1

diff = 0
for i in left:
    diff += i * right[i]

print(diff)