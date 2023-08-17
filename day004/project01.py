# Rock Paper Sisssors Game
import random

print("Welcome to the game")
print("Rock Paper Sisssors Game")
print("Choose one of the following")
print("1. Rock")
print("2. Paper")
print("3. Sisssors")
print("4. Exit")

desc_win = "You win"

while True:
    user_input = int(input("Enter your choice: "))
    if user_input == 4:
        print("Thank you for playing")
        break
    if user_input < 1 or user_input > 4:
        print("Invalid choice")
        continue

    computer_choice = random.randint(1, 3)
    print(f"Computer choice: {computer_choice}")

    if user_input == computer_choice:
        print("Tie")
    elif user_input == 1 and computer_choice == 3:
        print(desc_win)
    elif user_input == 2 and computer_choice == 1:
        print(desc_win)
    elif user_input == 3 and computer_choice == 2:
        print(desc_win)
    else:
        print("You lose")
