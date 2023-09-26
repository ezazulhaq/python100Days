"""
You are given n words. Some words may repeat.
For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.

Sample Input:
4
bcdef
abcdefg
bcde
bcdef

Sample Output:
3
2 1 1
"""

n = int(input())
words = []
for _ in range(n):
    # print("hi")
    words.append(input())


def word_occurrences(words):
    word_dict = {}
    result = []
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
            result.append(word)
        else:
            word_dict[word] += 1
    print(len(word_dict))
    print(' '.join(str(word_dict[word]) for word in result))


word_occurrences(words)