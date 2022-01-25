import sys

fish = {}
for i in range(9):
    fish[i] = 0
for f in map(int, sys.stdin.readline().split(',')):
    fish[f] += 1

for _ in range(256):
    zero = fish[0]
    for i in range(1, 9):
        fish[i - 1] = fish[i]
    fish[6] += zero
    fish[8] = zero

print(sum(fish.values()))