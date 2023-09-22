"""
You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:
Here N = 6

1
22
333
4444
55555
"""

"""
Task
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those  integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
"""

n = int(input())
l = [i for i in range(1, n+1)]
t = tuple(l)
print(hash(t))
