"""
Task:
You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if P(x) = k.

Constraints:
All coefficients of polynomial P are integers.
x and y are also integers.

Input Format:
The first line contains the space separated values of x and k.
The second line contains the polynomial P.
"""

def verify_polynomial(x, k, P):
    if eval(P) == k:
        return True
    else:
        return False

x, k = map(int, input().split())
P = input().strip()
print(verify_polynomial(x, k, P))
