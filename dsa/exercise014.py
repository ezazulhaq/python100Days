"""
Given an array Arr of N positive integers. 
Your task is to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).

Note: There can be more than one element in the array which have the same value as its index. 
You need to include every such element's index. Follows 1-based indexing of the array.
"""


def value_equalto_index(arr):
    ans = []
    for i in range(len(arr)):
        if arr[i] == i+1:
            ans.append(i+1)
    return ans


arr = [5, 2, 45, 12, 7]
print(value_equalto_index(arr))
