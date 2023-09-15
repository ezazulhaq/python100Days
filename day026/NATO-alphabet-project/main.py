import pandas
import os
data_file_path = os.path.join(os.path.dirname(__file__), "nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
nato_df = pandas.read_csv(data_file_path)
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)
