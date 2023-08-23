# Number guessing Game
import random
import art
import game

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Set the random number
random_num = random.randint(1, 100)

# Set the difficulty level
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

game.guess_game(random_num, difficulty)
