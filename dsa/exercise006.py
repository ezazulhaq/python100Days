"""
Given a sorted array with possibly duplicate elements.
The task is to find indexes of first and last occurrences of an element X in the given array.

Note: If the element is not present in the array return {-1,-1} as pair.
"""


def indexes(arr, x):
    first = -1
    last = -1
    for i in range(len(arr)):
        if arr[i] == x:
            if first == -1:
                first = i
            last = i
    return [first, last]


arr = [1, 2, 2, 2, 3, 4, 7, 8, 8]
print(indexes(arr, 7))
