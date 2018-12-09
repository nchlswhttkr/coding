import sys


def matches(a, b):
    return abs(ord(a) - ord(b)) == 32


def main():
    processed = []
    for char in sys.stdin.readline().rstrip():
        if len(processed) >= 1 and matches(char, processed[-1]):
            processed.pop()
        else:
            processed.append(char)

    print(len(processed))


if __name__ == "__main__":
    main()
