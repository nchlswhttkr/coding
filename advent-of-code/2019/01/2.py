import sys

fuel_sum = 0
for mass in sys.stdin.readlines():
    fuel = int(mass) // 3 - 2
    while fuel > 0:
        fuel_sum += fuel
        fuel = fuel // 3 - 2
print(fuel_sum)
