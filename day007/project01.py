# Hangman game
import random

# Store a group of words in a list
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the list
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)

# Create a blank word of the same length as the chosen word
blank_word = []
for letter in range(word_length):
    blank_word.append("_")

life_count = 6
print(f"You have {life_count} lives")

while life_count > 0:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            blank_word[position] = guess

    print(blank_word)

    # Reduce life_count by 1 if the letter the user guessed is not in the chosen_word
    if guess not in chosen_word:
        print("You guessed wrong")
        life_count -= 1
        print(f"You have {life_count} lives left")

    # check if blnk_word have any '_' in it
    if "_" not in blank_word:
        print("You win")
        break

if life_count == 0:
    print("You lose")
