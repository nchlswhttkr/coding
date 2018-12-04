import sys


def main():
    acc = 0
    for line in sys.stdin.readlines():
        acc += int(line)
    print(acc)


if __name__ == "__main__":
    main()
