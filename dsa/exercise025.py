"""
Given two strings a and b. The task is to find if the string 'b' can be obtained 
by rotating (in any direction) string 'a' by exactly 2 places.
"""


def is_rotated(str1, str2):
    if len(str1) != len(str2) or str1 == str2 or len(str1) <= 2:
        return False

    str1 = str1 * 2
    if str1.find(str2) != - 1:
        return True
    return False


print(is_rotated("tix", "tix"))
