"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring:
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Function Description:
Complete the minion_game in the editor below.
minion_game has the following parameters:
- string string: the string to analyze

Prints
- string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
"""

def minion_game(string):
    vowels = 'AEIOU'
    kevin_score, stuart_score = 0, 0
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
            kevin_score += (length - i)
        else:
            stuart_score += (length - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)