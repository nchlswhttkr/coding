import sys

valid = 0
for passport in ''.join(sys.stdin.readlines()).split("\n\n"):
    if "byr:" not in passport:
        pass
    elif "iyr:" not in passport:
        pass
    elif "eyr:" not in passport:
        pass
    elif "hgt:" not in passport:
        pass
    elif "hcl:" not in passport:
        pass
    elif "ecl:" not in passport:
        pass
    elif "pid:" not in passport:
        pass
    else:
        valid += 1
print(valid)
