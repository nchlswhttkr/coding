import sys


def contains(numbers, target, start, end):
    for i in range(start, end - 1):
        for j in range(i + 1, end):
            if target == numbers[i] + numbers[j]:
                return True
    return False


numbers = [int(i) for i in sys.stdin.readlines()]

i = 25
while contains(numbers, numbers[i], i - 25, i):
    i += 1
print(numbers[i])
