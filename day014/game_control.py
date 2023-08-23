import random
from store import data


def game_start(choice_a, score):
    choice_b = random.choice(data)
    while choice_a == choice_b:
        choice_b = random.choice(data)

    print(f"Your score is {score}.")
    print(f"{choice_a['name']}, {choice_a['description']}")
    print("Vs")
    print(f"{choice_b['name']}, {choice_b['description']}\n")

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_input == "a" and choice_a['follower_count'] > choice_b['follower_count']:
        print("You win!")
        score += 1
        choice_a = choice_b
        game_start(choice_a, score)

    elif user_input == "b" and choice_b['follower_count'] > choice_a['follower_count']:
        print("You win!\n")
        score += 1
        game_start(choice_a, score)

    else:
        print("You lose!")
        print(f"Your final score is {score}")
