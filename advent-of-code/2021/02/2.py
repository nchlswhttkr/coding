import sys

depth = 0
position = 0
aim = 0
for line in sys.stdin.readlines():
    command, value = line.split()
    if command == "forward":
        position += int(value)
        depth += aim * int(value)
    elif command == "down":
        aim += int(value)
    elif command == "up":
        aim -= int(value)

print(depth * position)