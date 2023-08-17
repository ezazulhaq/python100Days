# Find the Average height of students in the class.

# Input student heights in a list.
student_heights = input("Input a list of student heights : ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])  # type: ignore
print(student_heights)

# Calculate the sum of the heights.
total_height = 0
for height in student_heights:
    total_height += height  # type: ignore

average_height = round(total_height / len(student_heights))

print(f"Average height of students in the class is {average_height}")
