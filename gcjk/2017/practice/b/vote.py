if __name__ == "__main__":

    T = int(input())

    for case in range(1, T + 1):
        A, B = input().split()
        A, B = int(A), int(B)
        probability = (A - B) / (A + B)
        print("Case #{}: {}".format(case, probability))
