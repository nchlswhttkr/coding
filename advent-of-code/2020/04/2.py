import re
import sys


def validate(passport, field, validator):
    match = re.search("{}:([^\n ]*)".format(field), passport)
    if match is not None:
        return validator(match[1])
    return False


valid = 0
for passport in ''.join(sys.stdin.readlines()).split("\n\n"):
    if not validate(passport, "byr", lambda value: (1920 <= int(value) <= 2002)):
        pass
    elif not validate(passport, "iyr", lambda value: (2010 <= int(value) <= 2020)):
        pass
    elif not validate(passport, "eyr", lambda value: (2020 <= int(value) <= 2030)):
        pass
    elif not validate(passport, "hgt", lambda value: ((150 <= int(value.strip("cm")) <= 193)) if value[-2:] == "cm" else (59 <= int(value.strip("in")) <= 76)):
        pass
    elif not validate(passport, "hcl", lambda value: re.fullmatch("#[0-9a-f]{6}", value)):
        pass
    elif not validate(passport, "ecl", lambda value: value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        pass
    elif not validate(passport, "pid", lambda value: re.fullmatch("[0-9]{9}", value)):
        pass
    else:
        valid += 1
print(valid)
