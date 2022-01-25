import sys

lines = [line.strip() for line in sys.stdin.readlines()]
counters = [0] * len(lines[0])

for line in lines:
    for i in range(len(line)):
        counters[i] += 1 if line[i] == '1' else -1

gamma = int(''.join(['1' if c > 0 else '0' for c in counters]), 2)
epsilon = (2 ** len(counters)) - 1 - gamma

print(gamma * epsilon)
        