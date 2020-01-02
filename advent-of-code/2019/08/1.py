import sys

WIDTH = 25
HEIGHT = 6


def get_occurences(l, n):
    def is_n(x):
        return x == n
    return len([i for i in filter(is_n, l)])


image = sys.stdin.readline().rstrip()

layers = []  # list of list for layers of pixels
for i in range(len(image)):
    if i % (HEIGHT * WIDTH) == 0:
        layers.append([image[i]])
    else:
        layers[-1].append(image[i])

fewest_zeroes = 0
for i in range(1, len(layers)):
    if get_occurences(layers[i], '0') < get_occurences(layers[fewest_zeroes], '0'):
        fewest_zeroes = i

print(get_occurences(layers[fewest_zeroes], '1') *
      get_occurences(layers[fewest_zeroes], '2'))
