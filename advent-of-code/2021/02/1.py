import sys

depth = 0
position = 0
for line in sys.stdin.readlines():
    command, value = line.split()
    if command == "forward":
        position += int(value)
    elif command == "down":
        depth += int(value)
    elif command == "up":
        depth -= int(value)

print(depth * position)