import sys


def main():
    islands = 0
    is_island = [[True if island == '1' else False for island in row.split()]
                 for row in sys.stdin.readlines()]
    rows, columns = len(is_island), len(is_island[0])

    for i in range(rows):
        for j in range(columns):

            if is_island[i][j]:
                islands += 1
                is_island[i][j] = False
                stack = [(i, j)]

                # Traverse and flood surrounding islands
                while len(stack) != 0:
                    x, y = stack.pop()

                    if y > 0 and is_island[x][y - 1]:
                        is_island[x][y - 1] = False
                        stack.append((x, y - 1))

                    if y < columns - 1 and is_island[x][y + 1]:
                        is_island[x][y + 1] = False
                        stack.append((x, y + 1))

                    if x > 0 and is_island[x - 1][y]:
                        is_island[x - 1][y] = False
                        stack.append((x - 1, y))

                    if x < rows - 1 and is_island[x + 1][y]:
                        is_island[x + 1][y] = False
                        stack.append((x + 1, y))

    print(islands)


if __name__ == "__main__":
    main()
