"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
"""

arr = [2, 3, 6, 6, 5]
# find the second highest value in a array
arr = list(set(arr))
arr.sort(reverse=True)
print(arr[1])

