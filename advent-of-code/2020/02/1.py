import sys

passwords_valid = 0
for line in sys.stdin.readlines():
    [policy, password] = line.split(':')
    [limit, character] = policy.split()
    [lower, upper] = map(int, limit.split('-'))
    if lower <= password.count(character) <= upper:
        passwords_valid += 1
print(passwords_valid)
