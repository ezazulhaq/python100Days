"""
Given a non-empty array nums[] of integers of length N, find the top k elements which have the highest frequency in the array. 
If two numbers have same frequencies, then the larger number should be given more preference.
"""


def top_k(arr, k):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1

    print(freq)
    return sorted(freq, key=lambda x: (-freq[x], -x))[:k]


arr = [1, 1, 2, 2, 2, 3, 3, 4]
print(top_k(arr, 2))
