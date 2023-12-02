import sys

spelled_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

total = 0
for line in sys.stdin.readlines():
    first = None
    i = 0
    while first is None:
        if ord("0") <= ord(line[i]) <= ord("9"):
            first = int(line[i])
        elif line[max(0, i - 2) : i + 1] in spelled_digits:
            first = spelled_digits[line[max(0, i - 2) : i + 1]]
        elif line[max(0, i - 3) : i + 1] in spelled_digits:
            first = spelled_digits[line[max(0, i - 3) : i + 1]]
        elif line[max(0, i - 4) : i + 1] in spelled_digits:
            first = spelled_digits[line[max(0, i - 4) : i + 1]]
        i += 1

    last = first
    while i < len(line):
        if ord("0") <= ord(line[i]) <= ord("9"):
            last = int(line[i])
        elif line[max(0, i - 2) : i + 1] in spelled_digits:
            last = spelled_digits[line[max(0, i - 2) : i + 1]]
        elif line[max(0, i - 3) : i + 1] in spelled_digits:
            last = spelled_digits[line[max(0, i - 3) : i + 1]]
        elif line[max(0, i - 4) : i + 1] in spelled_digits:
            last = spelled_digits[line[max(0, i - 4) : i + 1]]
        i += 1

    total += first * 10 + last

print(total)
