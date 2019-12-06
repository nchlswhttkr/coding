
import sys

(lower, upper) = (int(i) for i in sys.stdin.readline().split('-'))


def satisfies(n):
    n = str(n)

    pair = False
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
        if pair == False and n[i] == n[i + 1]:
            pair = True

    return pair


count = 0
for i in range(lower, upper + 1):
    if satisfies(i):
        count += 1

print(count)
