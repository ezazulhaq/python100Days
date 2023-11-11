"""
Given a matrix(2D array) M of size N*N consisting of 0s and 1s only. 
The task is to find the column with maximum number of 0s. 
If more than one column exists, print the one which comes first. 
If the maximum number of 0s is 0 then return -1.
"""


def column_with_max_zeros(arr, n):
    max_zeros = 0
    max_zeros_col = -1
    for col in range(n):
        zeros = 0
        for row in range(n):
            if arr[row][col] == 0:
                zeros += 1
        if zeros > max_zeros:
            max_zeros = zeros
            max_zeros_col = col
    return max_zeros_col


arr = [[0, 0, 0],
       [1, 0, 1],
       [0, 1, 1]]
print(column_with_max_zeros(arr, 3))
