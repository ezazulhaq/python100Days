"""
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N.
Find the missing element.
"""


def find_missing(arr) -> int:
    n = len(arr) + 1
    total = n * (n + 1) // 2
    return total - sum(arr)


arr = [2]
print(find_missing(arr))
