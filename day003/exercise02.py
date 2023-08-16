# Leap year checker

# Allow to enter an year
year = int(input("Which year do you want to check? "))

# Check if the year is divisible by 4
if year % 4 == 0:
    # Check if the year is divisible by 100
    if year % 100 == 0:
        # Check if the year is divisible by 400
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")

else:
    print("Not leap year.")
