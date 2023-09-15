# Program to read two files and get common lines
# Code snippet from exercise02.py
# 
# # Create a Dataframe from scratch

# Read file 1
with open("./day026/file1.txt") as file1:
    file1_data = file1.readlines()

# Read file 2
with open("./day026/file2.txt") as file2:
    file2_data = file2.readlines()

print(file1_data)
print(file2_data)

result = [int(num) for num in file1_data if num in file2_data]
print(result)