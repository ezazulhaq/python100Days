# Higher Lower Game
from game_control import game_start
from store import data
import random

print("Welcome to Higher Lower Game!")
print("You have to guess the follower count of the chosen option.")
print("If you guess correctly, you will get a point and if you guess wrong, you will lose the game")
print("If you have guessed all the options correctly, you will win the game.")
print("Let's start!\n")

choice_a = random.choice(data)
score = 0
win_flag = True

game_start(choice_a, score)
