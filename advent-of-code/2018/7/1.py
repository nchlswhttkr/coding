import sys
import re
from queue import Queue


def main():
    dependents = [[] for _ in range(26)]
    remaining_dependees = [0]*26

    for line in sys.stdin.readlines():
        dependee, depender = (
            (ord(i) - 65) for i in re.search(r" ([A-Z]).*([A-Z])", line).group(1, 2))

        remaining_dependees[depender] += 1
        dependents[dependee].append(depender)

    for i in range(26):
        dependents[i] = sorted(dependents[i])

    ordered = ''
    while sum(remaining_dependees) > -26:

        i = 0
        while remaining_dependees[i] != 0:
            i += 1

        remaining_dependees[i] = -1
        ordered += chr(i + 65)
        for dependent in dependents[i]:
            remaining_dependees[dependent] -= 1

    print(ordered)


if __name__ == "__main__":
    main()
