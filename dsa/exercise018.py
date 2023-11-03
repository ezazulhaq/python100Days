"""
Given an array arr of n integers, write a function that returns true,
if there is a triplet (a, b, c) from the array (where a, b, and c are on different indexes)
that satisfies a2 + b2 = c2, otherwise return false.
"""


def check_triplet(arr):
    n = len(arr)
    squares = [x ** 2 for x in arr]
    counter = {}
    for i in squares:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    for i in range(n):
        for j in range(i + 1, n):
            sum_squares = squares[i] + squares[j]
            if sum_squares in counter and counter[sum_squares] > 0:
                return True

    return False


arr = [14, 17, 4, 4, 1, 9, 25, 12, 4, 9, 18, 15,
       12, 2, 3, 13, 16, 17, 15, 6, 5, 20, 14, 8]
print(check_triplet(arr))
