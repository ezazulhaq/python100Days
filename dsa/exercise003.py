"""
Given an array arr[] of n positive integers.
Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. 
Do the mentioned change in the array in-place.
"""

arr = [3, 5, 0, 0, 4]


def push_zeros_to_end(arr: list) -> None:
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1

    for num in arr:
        print(num, end=' ')


push_zeros_to_end(arr)
