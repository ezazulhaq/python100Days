"""
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, Return the index of any one of its peak elements.

Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0.

Inputs:
arr = [15]
arr = [1, 13]
arr = [1, 2, 3]
arr = [3, 4, 2]
"""


def peak_element(arr):
    if len(arr) == 1:
        return 0
    if arr[0] >= arr[1]:
        return 0
    if arr[-1] >= arr[-2]:
        return len(arr) - 1
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i - 1] and arr[i] >= arr[i + 1]:
            return i


arr = [1, 2, 2, 1]
print(peak_element(arr))
