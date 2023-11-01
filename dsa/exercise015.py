"""
Given a sorted array Arr of size N and a value X, 
find the number of array elements less than or equal to X 
and elements more than or equal to X. 

Examples:
Input:
N = 7, X = 5
Arr[] = {1, 2, 8, 10, 11, 12, 19}
Output: 2 5
Explanation: There are 2 elements less or
equal to 5 and 5 elements greater or equal
to 5.

"""


def get_more_less(arr, x):
    less = 0
    more = 0

    for i in arr:
        if i <= x:
            less += 1

        if i >= x:
            more += 1

    return less, more


arr = [1, 2, 8, 10, 11, 12, 19]
print(get_more_less(arr, 3))
