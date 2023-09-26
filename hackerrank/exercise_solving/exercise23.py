"""
s = "AAABCADDE" , n = 9
k = 3, then n/k = 3 substrings

There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'.
The first substring is all 'A' characters, so u1='A'. 
The second substring has all distinct characters, so u2='BCA'.
The third substring has  different characters, so u3=DE. 

Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.
"""

def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0, n, k):
        u = string[i:i+k]
        print(''.join(dict.fromkeys(u)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)