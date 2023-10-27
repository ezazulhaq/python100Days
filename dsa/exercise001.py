"""
Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. 
Return the answer in ascending order. 
If no such element is found, return list containing [-1]. 
"""


def find_duplicates(arr):
    hash_table = {}
    duplicates = []

    for num in arr:
        if num in hash_table:
            if hash_table[num] == 1:  # We only want to add duplicates once
                duplicates.append(num)
            hash_table[num] += 1
        else:
            hash_table[num] = 1

    duplicates.sort()

    if len(duplicates) == 0:
        return [-1]
    else:
        return duplicates


arr = [7, 6, 8, 4, 9, 8, 4, 7, 4, 4]
print(find_duplicates(arr))
