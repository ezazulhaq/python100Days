from typing import List
"""
You are given an array of N+2 integer elements.
All elements of the array are in the range 1 to N.
Also, all elements occur once except two numbers which occur twice.
Find the two repeating numbers.

Note: Return the numbers in their order of appearing twice.
So, if X and Y are the repeating numbers, and X repeats twice before Y repeating twice, then the order should be (X, Y).
"""


def find_repeating_numbers(arr: List[int]) -> List[int]:
    num_dict = {}
    order = []
    for num in arr:
        if num in num_dict:
            num_dict[num] += 1
            if num_dict[num] == 2:
                order.append(num)
        else:
            num_dict[num] = 1

    return order


arr = [1, 2, 2, 1]
print(find_repeating_numbers(arr))
