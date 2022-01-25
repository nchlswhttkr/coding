import sys

count = 0
for line in sys.stdin.readlines():
    for digit in line.strip().split('|')[1].split():
        if len(digit) in [2, 3, 4, 7]:
            count += 1
print(count)