def get_substring_sum(max_pairs):
    substrings = 0
    for pair in range(1, max_pairs + 1):
        substrings += pair
    return substrings

if __name__ == "__main__":

    T = int(input())

    for case in range(1, T + 1):
        L, R = input().split()
        max_pairs = min(int(L), int(R))
        print("Case #{}: {}".format(case, get_substring_sum(max_pairs)))
