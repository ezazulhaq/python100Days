student_d = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_d.items():
    print(key)
    print(value)

# Iterate over Pandas DataFrames
import pandas as pd

student_df = pd.DataFrame(student_d)
print(student_df)

# Iterate over rows of a Pandas DataFrame
for (index, row) in student_df.iterrows():
    print(row)
    print(row.student)
    print(row.score)