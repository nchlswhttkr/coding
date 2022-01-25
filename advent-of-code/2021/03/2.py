import sys

lines = [line.strip() for line in sys.stdin.readlines()]
counters = [0] * len(lines[0])

oxygen_values = [line for line in lines]
i = 0
while len(oxygen_values) > 1:
    count = 0
    for value in oxygen_values:
        count += 1 if value[i] == '1' else -1
    oxygen_values = list(filter(lambda x: x[i] == ('1' if count >= 0 else '0'), oxygen_values))
    i += 1

co2_values = [line for line in lines]
i = 0
while len(co2_values) > 1:
    count = 0
    for value in co2_values:
        count += 1 if value[i] == '1' else -1
    co2_values = list(filter(lambda x: x[i] == ('0' if count >= 0 else '1'), co2_values))
    i += 1

print(int(''.join(oxygen_values[0]), 2) * int(''.join(co2_values[0]), 2))
        