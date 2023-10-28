"""
You are given a string ‘str’, the task is to check that reverses of all possible substrings of ‘str’ are present in ‘str’.
If yes then the answer is 1, otherwise, the answer will be 0.
"""


def is_reversible(str):
    if str == str[::-1]:
        return 1
    else:
        return 0


print(is_reversible("bfgfb"))
