"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example
[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
"""

def second_lowest_students(students):
    # Sort the list by grades
    students.sort(key = lambda x: x[1])
    
    # Get the second lowest grade
    second_lowest = sorted(list(set([x[1] for x in students])))[1]
    
    # Get the names of students with the second lowest grade
    second_lowest_students = [x[0] for x in students if x[1] == second_lowest]
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    
    # Print each name on a new line
    for student in second_lowest_students:
        print(student)

# Test the function
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
second_lowest_students(students)