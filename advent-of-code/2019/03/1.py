import sys


wires = sys.stdin.readlines()

# initial pass to get bounds of field
x_lower, x_upper = 0, 0
y_lower, y_upper = 0, 0
for wire in wires:
    x, y = 0, 0
    for command in wire.split(','):
        direction, magnitude = command[0], int(command[1:])
        if direction == 'R':
            x += magnitude
            x_upper = max(x_upper, x)
        if direction == 'L':
            x -= magnitude
            x_lower = min(x_lower, x)
        if direction == 'U':
            y += magnitude
            y_upper = max(y_upper, y)
        if direction == 'D':
            y -= magnitude
            y_lower = min(y_lower, y)

# make the field itself
field = [[False] * (y_upper-y_lower+1) for _ in range(x_upper-x_lower+1)]

# starting from the origin, lay out the first wire
x, y = abs(x_lower), abs(y_lower)
for command in wires[0].split(','):
    direction, magnitude = command[0], int(command[1:])

    # determine how we displace when stepping
    if direction == 'R':
        displacement = (1, 0)
    if direction == 'L':
        displacement = (-1, 0)
    if direction == 'U':
        displacement = (0, 1)
    if direction == 'D':
        displacement = (0, -1)

    # mark each step
    for _ in range(magnitude):
        x += displacement[0]
        y += displacement[1]
        field[x][y] = True

# lay out the second wire from the origin, checking for the closest intersection
x, y = abs(x_lower), abs(y_lower)
shortest_distance = None
for command in wires[1].split(','):
    direction, magnitude = command[0], int(command[1:])

    # determine how we displace when stepping
    if direction == 'R':
        displacement = (1, 0)
    if direction == 'L':
        displacement = (-1, 0)
    if direction == 'U':
        displacement = (0, 1)
    if direction == 'D':
        displacement = (0, -1)

    # check for intersections at each step
    for _ in range(magnitude):
        x += displacement[0]
        y += displacement[1]
        if field[x][y]:
            distance = abs(x + x_lower) + abs(y + y_lower)
            if shortest_distance is None or distance < shortest_distance:
                shortest_distance = distance

print(shortest_distance)
