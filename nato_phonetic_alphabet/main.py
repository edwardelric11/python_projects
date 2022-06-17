# NATO Alphabet

import pandas as pd

CSV_FILE = "nato_phonetic_alphabet.csv"


def get_input():
    """Gets input from the user, turns it into uppercase and returns it as STR."""
    while True:
        text = input("> ").upper()
        if text == "":
            print(f"Please enter a word.")
        else:
            return text


# create a data frame from the csv file
codes_df = pd.read_csv(CSV_FILE)

# create a dictionary using a dictionary comprehension
codes_dict = {row.letter: row.code for (index, row) in codes_df.iterrows()}


print("Enter a word to convert:")
word = get_input()

# Create a list of the phonetic code words from the input word, ignore anything other than letters
output = [codes_dict[char] for char in word if char in codes_dict]

# print the result in a more human friendly format
if len(output) > 0:
   print(" ".join(output))

print("Goodbye.")
