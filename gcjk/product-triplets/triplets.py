from math import factorial

LIMIT = 2 * 10**5


def naive(A):
    triplets = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            for k in range(j + 1, len(A)):
                if A[i]*A[j] == A[k] or A[i]*A[k] == A[j] or A[j]*A[k] == A[i]:
                    triplets += 1
    return triplets


def count_triplets(unsorted):
    A = sorted(unsorted, reverse=True)

    triplets = 0
    instances = [0] * (LIMIT + 1)

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            product = A[i] * A[j]
            if 0 < product <= LIMIT:
                triplets += instances[A[i] * A[j]]
        instances[A[i]] += 1

    def c(n, r):  # combinations of R selections from N
        return factorial(n) // (factorial(r) * factorial(n-r))

    if A[-2] == 0:  # at least two 0s
        nonzeroes = A.index(0)
        triplets += nonzeroes * c(len(A) - nonzeroes, 2)

    if A[-3] == 0:  # at least three 0s
        triplets += c(len(A) - A.index(0), 3)

    return triplets


def main():
    for T in range(1, int(input()) + 1):
        input()
        print('Case #{}: {}'.format(T, count_triplets(
            [int(i) for i in input().split()])))


if __name__ == "__main__":
    main()
