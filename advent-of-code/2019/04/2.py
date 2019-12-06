
import sys

(lower, upper) = (int(i) for i in sys.stdin.readline().split('-'))


def satisfies(n):
    n = str(n)
    occurences = {}
    for c in n:
        if c in occurences:
            occurences[c] += 1
        else:
            occurences[c] = 1
    return n == ''.join(sorted(n)) and 2 in occurences.values()


count = 0
for i in range(lower, upper + 1):
    if satisfies(i):
        count += 1

print(count)
