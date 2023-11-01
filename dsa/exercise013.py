"""
Given an array Arr of size N, print second largest distinct element from an array.
"""


def second_largest(arr):
    a = list(set(arr))

    if len(a) == 1:
        return -1

    a.sort()
    return a[-2]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(second_largest(arr))
