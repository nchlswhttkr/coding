import sys
import re


def main():
    fabric_cuts = [[0]*1000 for _ in range(1000)]

    for cut in sys.stdin.readlines():

        match = re.match(
            r"#[0-9]+ @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)", cut)
        x_off, y_off, x_len, y_len = (int(group)
                                      for group in match.group(1, 2, 3, 4))

        for x in range(x_off, x_off + x_len):
            for y in range(y_off, y_off + y_len):
                fabric_cuts[x][y] += 1

    acc = 0
    for i in range(1000):
        for j in range(1000):
            acc += 1 if fabric_cuts[i][j] >= 2 else 0
    print(acc)


if __name__ == "__main__":
    main()
