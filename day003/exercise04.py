# Love Calculator program

# Enter the name of first person
name1 = input("Enter the name of first person: ")

# Enter the name of second person
name2 = input("Enter the name of second person: ")

# Combine both names to make a single string
combined_names = name1 + name2

# Convert the string to lower case
combined_names = combined_names.lower()

# Count the number of letters in the string
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

true = t + r + u + e

# Count the number of letters in the string
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love = l + o + v + e

# Combine the numbers to make a single number
love_score = int(str(true) + str(love))

# Check if the love score is less than 10 or greater than 90
if love_score < 10 or love_score > 90:
    print(
        f"Your love score is {love_score}, you go together like coke and mentos.")

# Check if the love score is between 40 and 50
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, you are alright together.")

# Check if the love score is between 10 and 40
else:
    print(f"Your love score is {love_score}.")

# End of program
