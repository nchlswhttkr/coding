import sys

seen = set()
for n in map(int, sys.stdin.readlines()):
    seen.add(n)
    if 2020 - n in seen:
        print(n * (2020 - n))
        break
