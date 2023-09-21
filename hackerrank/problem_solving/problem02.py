"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

0.400000
0.400000
0.200000
"""

arr = [-4, 3, -9, 0, 4, 1]

def plus_minus(arr: list):
    # Write your code here
    # get the list of postives, negatives and zeros count from a list
    positive_ratio = len([num for num in arr if num > 0])/len(arr)
    print(f'{positive_ratio:.6f}')

    negative_ratio = len([num for num in arr if num < 0])/len(arr)
    print(f'{negative_ratio:.6f}')

    zero_ratio = len([num for num in arr if num == 0])/len(arr)
    print(f'{zero_ratio:.6f}')



plus_minus(arr)