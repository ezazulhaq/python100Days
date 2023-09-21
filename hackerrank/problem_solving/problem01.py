"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .
"""

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonal_difference(arr):
    # Write your code here
    print(arr)
    # we have 3x3 matrix
    # so we need to calculate the sum of the left to right and right to left diagonals
    left_to_right_diagonal_sum = 0
    right_to_left_diagonal_sum = 0


    for i in range(len(arr)):
        left_to_right_diagonal_sum += arr[i][i]
        right_to_left_diagonal_sum += arr[i][len(arr)-i-1]

    return abs(left_to_right_diagonal_sum - right_to_left_diagonal_sum)


if __name__ == '__main__':

    arr = [[3, 5, 6], [1, 6, 4], [4, 7, 9]]

    result = diagonal_difference(arr)

    print(result)
