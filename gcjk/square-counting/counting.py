def get_squares(R, C):

    mod = 1000000007

    A, B = max(R, C), min(R, C)
    i = B - 1
    squares = (A * B) * i*(i+1)//2 -  \
              (A + B) * (2*i+1)*(i+1)*i//6 + \
              (i**4+2*i**3+i**2)//4

    return squares % mod


if __name__ == "__main__":

    T = int(input())

    for case in range(1, T + 1):
        R, C = input().split()
        R, C = int(R), int(C)
        print("Case #{}: {}".format(case, get_squares(R, C)))