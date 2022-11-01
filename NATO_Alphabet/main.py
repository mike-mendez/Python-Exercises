import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {}
for index, row in data.iterrows():
    data_dict[row.letter] = row.code

user_word = input("Enter a word:\t").upper()
letters = [letter for letter in user_word]

nato_callout = [data_dict[letter] for letter in user_word]
