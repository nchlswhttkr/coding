from random import randint


def find_missing(arr):
    acc = 1
    for i in range(len(arr)):
        acc += i + 2
        acc -= arr[i]
    return acc


def main():
    arr = []
    N = 10
    for i in range(N):
        arr.insert(randint(0, i), i + 1)
    arr.pop()
    print(arr)
    print(find_missing(arr))


if __name__ == "__main__":
    main()
