if __name__ == '__main__':
    for i in range(1, 101):
        out = ''
        if (i % 3 == 0):
            out += 'Fizz'
        if (i % 5 == 0):
            out += 'Buzz'
        print(i if len(out) == 0 else out)
