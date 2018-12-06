import sys


def main():
    changes = [int(line) for line in sys.stdin]
    acc = 0
    freq = {}
    i = 0
    while acc not in freq:
        freq[acc] = True
        acc += changes[i]
        i = (i + 1) % len(changes)
    print(acc)


if __name__ == "__main__":
    main()
