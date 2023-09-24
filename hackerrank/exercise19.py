"""
Task

You are given a string S.
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string S.
"""

if __name__ == '__main__':
    s = input()

    has_alnum = has_alpha = has_digit = has_lower = has_upper = False

    for i in s:
        if i.isalnum():
            has_alnum = True
        if i.isalpha():
            has_alpha = True
        if i.isdigit():
            has_digit = True
        if i.islower():
            has_lower = True
        if i.isupper():
            has_upper = True

    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)

