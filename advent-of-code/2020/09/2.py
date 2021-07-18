import sys


def contains(numbers, target, start, end):
    for i in range(start, end - 1):
        for j in range(i + 1, end):
            if target == numbers[i] + numbers[j]:
                return True
    return False


target = int(sys.argv[1])
numbers = [int(i) for i in sys.stdin.readlines()]
sums = []
i = 0
while target not in sums:
    sums.append(0)
    for s in range(len(sums)):
        sums[s] += numbers[i]
    i += 1

index = sums.index(target)
print(min(numbers[index:i]) + max(numbers[index:i]))
