import sys

seen = set()
for n1 in map(int, sys.stdin.readlines()):
    for n2 in seen:
        if 2020 - n1 - n2 in seen:
            print(n1 * n2 * (2020 - n1 - n2))
            break
    seen.add(n1)
