# find the average marks of selected students

student_marks = {
    "Krishna": [67,68.5,69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

query_name = input()

marks = student_marks[query_name]
avg_marks = sum(marks)/len(marks)
print(f"{avg_marks:.2f}")