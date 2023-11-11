"""
Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.

If the characters in str1 can be changed to get str2, then two strings, str1 and str2, are isomorphic. 
A character must be completely swapped out for another character while maintaining the order of the characters. 
A character may map to itself, but no two characters may map to the same character.
"""


def are_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False

    map_str1 = {}
    map_str2 = {}

    for i in range(len(str1)):
        if str1[i] in map_str1:
            if map_str1[str1[i]] != str2[i]:
                return False
        else:
            map_str1[str1[i]] = str2[i]

        if str2[i] in map_str2:
            if map_str2[str2[i]] != str1[i]:
                return False
        else:
            map_str2[str2[i]] = str1[i]

    return True


print(are_isomorphic("airg", "dphc"))
