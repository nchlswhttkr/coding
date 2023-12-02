import sys

total = 0
for line in sys.stdin.readlines():
    numbers = list(filter(lambda x: ord("0") <= ord(x) <= ord("9"), line))
    total += int(numbers[0] + numbers[-1])

print(total)
