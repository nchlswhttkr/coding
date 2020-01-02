import sys

WIDTH = 25
HEIGHT = 6

out = ['2'] * WIDTH * HEIGHT
image = sys.stdin.readline().rstrip()

for i in range(len(image)):
    if out[i % (WIDTH * HEIGHT)] == '2':
        out[i % (WIDTH * HEIGHT)] = image[i]

for row in range(HEIGHT):
    for col in range(WIDTH):
        print('.' if out[row * WIDTH + col] == '1' else ' ', end='')
    print('', flush=True)
