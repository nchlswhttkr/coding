import sys

def solve(signals, display):
    one = next(filter(lambda x: len(x) == 2, signals))
    four = next(filter(lambda x: len(x) == 4, signals))
    seven = next(filter(lambda x: len(x) == 3, signals))
    eight = next(filter(lambda x: len(x) == 7, signals))
    
    a = next(filter(lambda x: x not in one, seven))

    signals_of_length_five = list(filter(lambda x: len(x) == 5, signals))
    d = list(four & signals_of_length_five[0] & signals_of_length_five[1] & signals_of_length_five[2])[0]
    g = list(signals_of_length_five[0] & signals_of_length_five[1] & signals_of_length_five[2] - {d, a})[0]

    e = list(eight - four - {a, g})[0]

    two = next(filter(lambda x: e in x, signals_of_length_five))
    c = list(two - {a, d, e, g})[0]
    three_and_five = list(filter(lambda x: e not in x, signals_of_length_five))
    f = list(three_and_five[0] & three_and_five[1] - {a, d, g})[0]
    b = list(four - {c, d, f})[0]

    zero = {a, b, c, e, f, g}
    three = {a, c, d, f, g}
    five = {a, b, d, f, g}
    six = {a, b, d, e, f, g}
    nine = {a, b, c, d, f, g}

    digits = [zero, one, two, three, four, five, six, seven, eight, nine]
    
    return int(''.join(list(map(lambda x: str(digits.index(x)), display))))

count = 0
for line in sys.stdin.readlines():
    signals, digits = line.strip().split(' | ')
    count += solve(list(map(set, signals.split())), list(map(set, digits.split())))
print(count)