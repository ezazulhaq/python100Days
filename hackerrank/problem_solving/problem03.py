"""
Staircase detail

This is a staircase of size :

   #
  ##
 ###
####
Its base and height are both equal to . It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .
"""

def staircase(n):
    i=0
    j=n

    while i != n and j!=0:
        i = i+1
        j = j-1
        
        for _ in range(j):
            print(" ", end="")
        for _ in range(i):
            print("#", end="")
        print()


staircase(4)