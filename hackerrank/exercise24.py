"""
Task

You are given the coefficients of a polynomial P.
Your task is to find the value of  at point x.

Input Format

The first line contains the space separated value of the coefficients in P.
The second line contains the value of x.
"""

import numpy

arr = list(map(float, input().split()))
x = int(input())
print(numpy.polyval(arr, x))