"""
Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward from that element. 
This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array (starting from the first element). 
If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.
"""


def min_jumps(arr):
    if len(arr) == 1:
        return 0
    if arr[0] == 0:
        return -1
    jumps = 1
    max_reach = arr[0]
    step = arr[0]
    for i in range(1, len(arr)):
        if i == len(arr) - 1:
            return jumps
        max_reach = max(max_reach, i + arr[i])
        step -= 1
        if step == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            step = max_reach - i
    return jumps


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(min_jumps(arr))
