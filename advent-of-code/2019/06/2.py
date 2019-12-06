import sys

planets = {}
for pair in sys.stdin.readlines():
    parent, child = pair.strip().split(')')
    planets[child] = parent

santa_path = []
child = 'SAN'
while child in planets:
    santa_path.append(planets[child])
    child = planets[child]

you_path = []
child = 'YOU'
while child in planets:
    you_path.append(planets[child])
    child = planets[child]

s, y = len(santa_path) - 1, len(you_path) - 1
while santa_path[s] == you_path[y]:
    s -= 1
    y -= 1

print(s + y + 2)  # adding 2 for the jump to a parent from YOU and SAN
