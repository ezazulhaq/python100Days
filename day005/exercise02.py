# Find the Highest Score of students in the class.

# Input student heights in a list.
student_scores = input("Input a list of student scores : ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])  # type: ignore
print(student_scores)

# Find the highest score.
highest_score = 0
for score in student_scores:
    if score > highest_score:  # type: ignore
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
