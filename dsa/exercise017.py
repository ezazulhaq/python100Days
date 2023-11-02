"""
You are given an array a, of n elements. 
Find the minimum index based distance between two distinct elements of the array, x and y. 
Return -1, if either x or y does not exist in the array.

Example:
Input:
N = 4
A[] = {1,2,3,2}
x = 1, y = 2
Output: 1
Explanation: x = 1 and y = 2. There are
two distances between x and y, which are
1 and 3 out of which the least is 1.
"""


def min_distance(arr, x, y):
    # check if x and y exist in the array
    if x not in arr or y not in arr:
        return -1

    # get the indices of x and y
    x_indices = [i for i, val in enumerate(arr) if val == x]
    y_indices = [i for i, val in enumerate(arr) if val == y]

    # get the minimum distance between x and y
    min_dist = float('inf')
    for i in x_indices:
        for j in y_indices:
            min_dist = min(min_dist, abs(i - j))

    return min_dist if min_dist != float('inf') else -1


arr = [1, 3, 3, 6, 3, 2]
print(min_distance(arr, 2, 3))
