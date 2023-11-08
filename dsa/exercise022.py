import numpy as n
"""
Given a matrix of size N x N. 
Print the elements of the matrix in the snake like pattern depicted below.

Example:
Input:
N = 3 
matrix[][] = {{45, 48, 54},
             {21, 89, 87}
             {70, 78, 15}}
Output: 
45 48 54 87 89 21 70 78 15 
Explanation:
Matrix is as below:
45 48 54
21 89 87
70 78 15
Printing it in snake pattern will lead to 
the output as 45 48 54 87 89 21 70 78 15.
"""


def snake_pattern(mat):
    ans = []
    # Iterate from first element of matrix
    for i in range(len(mat)):
        if i % 2 == 0:
            for j in range(len(mat[i])):
                ans.append(mat[i][j])
        else:
            for j in range(len(mat[i]) - 1, -1, -1):
                ans.append(mat[i][j])

    return ans


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print(snake_pattern(mat=mat))
