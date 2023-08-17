# Who will pay the bill program
import random

names_string = input("Give me everybody's names, separated by a comma. : ")
names = names_string.split(", ")

# person_who_will_pay = names[random.randint(0, len(names) - 1)]
# Alternative solution
person_who_will_pay = random.choice(names)

print(f"{person_who_will_pay.capitalize()} is going to buy the meal today!")
