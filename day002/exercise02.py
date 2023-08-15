# Prompt for Two digit number input
number = input("Enter a two digit number: ")

# Convert to string
number = str(number)

# Take each character and convert to int
first_digit = int(number[0])
second_digit = int(number[1])

# Sum the two digits
sum = first_digit + second_digit

# Print the sum
print(sum)
# End of program
