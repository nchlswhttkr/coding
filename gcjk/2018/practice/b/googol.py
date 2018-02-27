import math


def calculate_googol_string(K, flip_occurences=0):
    assert K > 0, 'K must be greater than 0 to have a position on the Sgoogol string'
    middle = 2 ** math.floor(math.log2(K))
    offset = K - middle
    if offset == 0:
        return flip_occurences
    else:
        flip_occurences += 1
        reversed_position = middle - offset
        return calculate_googol_string(reversed_position, flip_occurences)


def main():
    for T in range(1, int(input()) + 1):
        K = int(input())
        print('Case #{}: {}'.format(T, calculate_googol_string(K) % 2))


if __name__ == '__main__':
    main()
