import sys


def matches(a, b):
    return abs(ord(a) - ord(b)) == 32


def main():
    polymer = sys.stdin.readline().rstrip()
    minimum = len(polymer)

    for i in range(26):
        processed = []

        for char in polymer.translate({(i + 65): None, (i + 97): None}):
            if len(processed) >= 1 and matches(char, processed[-1]):
                processed.pop()
            else:
                processed.append(char)

        minimum = min(minimum, len(processed))

    print(minimum)


if __name__ == "__main__":
    main()
