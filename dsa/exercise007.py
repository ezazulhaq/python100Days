"""
Given two sorted arrays of distinct elements.
There is only 1 difference between the arrays.
First array has one element extra added in between.
Find the index of the extra element.
"""


def find_extra_element(arr1, arr2):
    i = 0
    j = 0
    while i < len(arr2):
        if arr1[i] != arr2[j]:
            return i
        i += 1
        j += 1
    return j


arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 3]

print(find_extra_element(arr1, arr2))
