import sys


def main():
    twos, threes = 0, 0
    for box in sys.stdin:
        letters = {}
        for l in box:
            letters[l] = letters[l] + 1 if l in letters else 1
        twos += 1 if 2 in letters.values() else 0
        threes += 1 if 3 in letters.values() else 0
    print(twos * threes)


if __name__ == "__main__":
    main()
