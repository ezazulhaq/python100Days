# Number of days, weeks and months left if you live for 90 years.

# Input current age.
age = input("What is your current age? ")

# Calculate number of days, weeks, months left.
days = 365 * (90 - int(age))
weeks = 52 * (90 - int(age))
months = 12 * (90 - int(age))

# Print number of days, weeks, months left.
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
