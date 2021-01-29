import sys
import unittest
from copy import deepcopy


def rotate(arr):
    arr = deepcopy(arr)
    size = len(arr[0])
    for i in range(size // 2):
        for j in range(i, size - i - 1):
            (
                arr[i][i + j],
                arr[i + j][size - i - 1],
                arr[size - i - 1][size - i - 1 - j],
                arr[size - i - 1 - j][i],
            ) = (
                arr[size - i - 1 - j][i],
                arr[i][i + j],
                arr[i + j][size - i - 1],
                arr[size - i - 1][size - i - 1 - j],
            )
    return arr


class TestRotate(unittest.TestCase):
    def test_two_by_two(self):
        self.assertEqual([[3, 1], [4, 2]], rotate([[1, 2], [3, 4]]))

    def test_three_by_three(self):
        self.assertEqual(
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]], rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        )

    def test_four_by_four(self):
        self.assertEqual(
            [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]],
            rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]),
        )


def main():
    arr = []
    for line in sys.stdin.readlines():
        arr.append(line.split())
    for row in rotate(arr):
        print(" ".join(row))


if __name__ == "__main__":
    main()