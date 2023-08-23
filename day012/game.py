def guess_game(random_num, difficulty):
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == random_num:
            print(f"You got it! The answer was {random_num}.")
            break
        elif guess > random_num:
            print("Too high.")
        else:
            print("Too low.")

        attempts -= 1

    if attempts == 0:
        print("You've run out of guesses, you lose.")
