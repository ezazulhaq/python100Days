"""
Given an array of size N, find the number of distinct pairs {i, j} (i != j) in the array,
such that the sum of a[i] and a[j] is greater than 0.
"""


def valid_pair(arr):
    arr.sort()
    l = 0
    r = len(arr) - 1
    count = 0
    while l < r:
        if arr[l] + arr[r] > 0:
            count += r - l
            r -= 1
        else:
            l += 1
    return count


arr = [3, -2, 1]
print(valid_pair(arr))
