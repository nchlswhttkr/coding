import sys


def main():
    coordinates = [[int(i) for i in line.split(', ')]
                   for line in sys.stdin.readlines()]
    maximum = [max([c[0] for c in coordinates]) + 1,
               max([c[1] for c in coordinates]) + 1]
    grid = [[10000]*maximum[1] for _ in range(maximum[0])]

    for i in range(len(coordinates)):
        c = coordinates[i]
        for x in range(maximum[0]):
            for y in range(maximum[1]):
                grid[x][y] -= (abs(x - c[0]) + abs(y - c[1]))

    print(sum([sum([1 if i > 0 else 0 for i in row]) for row in grid]))


if __name__ == "__main__":
    main()
