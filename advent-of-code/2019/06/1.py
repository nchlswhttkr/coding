import sys

planets = {}
for pair in sys.stdin.readlines():
    parent, child = pair.strip().split(')')
    planets[child] = parent


orbits = 0
for child in planets.keys():
    while child in planets:
        orbits += 1
        child = planets[child]

print(orbits)
