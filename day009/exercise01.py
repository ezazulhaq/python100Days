# Grading Program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
    "Ginny": 93,
    "Fred": 78,
    "George": 85,
}

sutdent_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        sutdent_grades[student] = "Outstanding"
    elif score > 80:
        sutdent_grades[student] = "Exceeds Expectations"
    elif score > 70:
        sutdent_grades[student] = "Acceptable"
    else:
        sutdent_grades[student] = "Fail"

print(sutdent_grades)
