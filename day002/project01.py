# Tip Calculator

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

tip_amount = total_bill * (tip_percentage / 100)
total_bill_with_tip = total_bill + tip_amount

bill_per_person = round((total_bill_with_tip / num_people), 2)

print(f"Each person should pay: ${bill_per_person}")
