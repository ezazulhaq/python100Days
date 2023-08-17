# Create a password generator
import random

# Ask how many letter you like in your password
letters = int(input("How many letters do you want in your password? "))

# Ask how many numbers you like in your password
numbers = int(input("How many numbers do you want in your password? "))

# Ask how many symbols you like in your password
symbols = int(input("How many symbols do you want in your password? "))

# Create a list of letters, numbers and symbols
password_list = []

for i in range(letters):
    password_list.append(random.choice(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))

for i in range(numbers):
    password_list.append(random.choice("0123456789"))

for i in range(symbols):
    password_list.append(random.choice("!@#$%^&*()"))

# Shuffle the list
random.shuffle(password_list)

# Join the list to a string
password = "".join(password_list)

# Print the password
print(f"Generated Password is {password}")
