"""
Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

Example


All permutations of  are:
.

Print an array of the elements that do not sum to .

"""

def find_coordinates(x, y, z, n):
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)]

x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = find_coordinates(x, y, z, n)
print(coordinates)