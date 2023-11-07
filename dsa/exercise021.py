"""
Given a square matrix of size N*N, print the sum of upper and lower triangular elements.
Upper Triangle consists of elements on the diagonal and above it.
The lower triangle consists of elements on the diagonal and below it. 
"""


def sum_triangles(matrix, n):
    upper = 0
    lower = 0
    for i in range(n):
        for j in range(n):
            if i <= j:
                upper += matrix[i][j]
            if i >= j:
                lower += matrix[i][j]
    return upper, lower


matrix = [[6, 5, 4],
          [1, 2, 5],
          [7, 9, 7]]

print(sum_triangles(matrix, 3))
