"""
Given a sorted array containing only 0s and 1s, find the transition point, 
i.e., the first index where 1 was observed, and before that, only 0 was observed.
"""


def transition_point(arr):
    for i in range(len(arr)):
        if arr[i] == 1:
            return i
    return -1


arr = [0, 0, 0, 1, 1]
print(transition_point(arr))
