import sys


def evaluate_square(grid, x, y, coordinate_name, distance):

    # outside bounds
    if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
        return False

    target = grid[x][y]

    # squares closer to another region center
    if target is not None and target[1] < distance:
        was_overwritten = False

    else:
        was_overwritten = True
        # empty square or square that is too far from another target
        if target is None or target[1] > distance:
            target = (coordinate_name, distance)
        # square in a different region
        elif target[0] != coordinate_name:
            target = (-1, distance)

    grid[x][y] = target
    return was_overwritten


def main():
    coordinates = [[int(i) for i in line.split(', ')]
                   for line in sys.stdin.readlines()]
    dimensions = [max([c[0] for c in coordinates]) + 1,
                  max([c[1] for c in coordinates]) + 1]

    # Squares in a grid are either NULL or a tuple, containing the region ID
    # and the distance from the center of that region
    grid = [[None]*dimensions[1] for _ in range(dimensions[0])]

    # Assign squares to their closest region
    for i in range(len(coordinates)):
        c = coordinates[i]

        # Move outwards from the region center until the region stops expanding
        radius = 0
        overwritten = True
        while overwritten:

            overwritten = False
            for x in range(0, radius + 1):
                y = radius - x

                overwritten = evaluate_square(
                    grid, c[0] - x, c[1] - y, i, radius) or overwritten
                overwritten = evaluate_square(
                    grid, c[0] + x, c[1] - y, i, radius) or overwritten
                overwritten = evaluate_square(
                    grid, c[0] - x, c[1] + y, i, radius) or overwritten
                overwritten = evaluate_square(
                    grid, c[0] + x, c[1] + y, i, radius) or overwritten

            radius += 1

    # Measure size of the region for each center
    counters = [0] * (len(coordinates) + 1)  # disputed regions
    for row in grid:
        for col in row:
            counters[col[0]] += 1

    # Disqualify points with regions extending infinitely
    for i in range(dimensions[0]):
        counters[grid[0][i][0]] = 0
        counters[grid[-1][i][0]] = 0
    for i in range(dimensions[1]):
        counters[grid[i][0][0]] = 0
        counters[grid[i][-1][0]] = 0

    # Largest finite region
    print(max(counters[:-1]))


if __name__ == "__main__":
    main()
