import sys
import re


def main():
    fabric_cuts = [[0]*1000 for _ in range(1000)]
    isolated_cuts = [False]

    for cut in sys.stdin:

        match = re.match(
            r"#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)", cut)
        cut_id, x_off, y_off, x_len, y_len = (
            int(group) for group in match.group(1, 2, 3, 4, 5))

        isolated_cuts.append(True)
        for x in range(x_off, x_off + x_len):
            for y in range(y_off, y_off + y_len):
                first_cut_id = fabric_cuts[x][y]
                if first_cut_id == 0:
                    fabric_cuts[x][y] = cut_id
                else:
                    isolated_cuts[first_cut_id] = False
                    isolated_cuts[cut_id] = False

    for i in range(len(isolated_cuts)):
        if isolated_cuts[i] == True:
            print(i)


if __name__ == "__main__":
    main()
