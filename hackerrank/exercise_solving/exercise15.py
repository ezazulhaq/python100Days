"""
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""

def split_and_join(line: str):
    # write your code here
    a = line.split(" ")
    return "-".join(a)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)