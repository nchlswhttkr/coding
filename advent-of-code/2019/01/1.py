import sys

fuel_sum = 0
for mass in sys.stdin.readlines():
    fuel_sum += int(mass) // 3 - 2
print(fuel_sum)
