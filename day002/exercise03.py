# BMI Calcuator

# Prompt for height
height = float(input("Enter your height in m: "))

# Prompt for weight
weight = float(input("Enter your weight in kg: "))

# Calculate BMI
bmi = round(weight / (height ** 2))

# Print BMI
print(f"Your BMI is {bmi}")

# Check BMI
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are normal weight.")
elif bmi < 30:
    print("You are overweight.")
elif bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")
