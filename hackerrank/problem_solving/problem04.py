"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
"""

arr = [1, 2, 3, 4, 5]

def mini_max_sum(arr):
    # Write your code here
    sum_arr = []

    for i in range(len(arr)):
        sum_arr.append(sum(arr[:i] + arr[i+1:]))
    print(f"{min(sum_arr)} {max(sum_arr)}")


mini_max_sum(arr)