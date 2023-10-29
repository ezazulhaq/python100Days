"""
Given an array arr[] and an integer K where K is smaller than size of array, 
the task is to find the Kth smallest element in the given array.
It is given that all array elements are distinct.

Note :-  l and r denotes the starting and ending index of the array.
"""


def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]


arr = [12, 3, 5, 7, 19]
k = 2
print(kth_smallest(arr, k))
