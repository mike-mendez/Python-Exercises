import pandas

data = pandas.read_csv("./data/nato_phonetic_alphabet.csv")
data_dict = {}
for index, row in data.iterrows():
    data_dict[row.letter] = row.code


def generate_nato_phonetic():
    user_word = input("Enter a word:\t").upper()
    try:
        nato_callout = [data_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_nato_phonetic()
    else:
        print(f"NATO Callout for {user_word} is:\t{nato_callout}")


generate_nato_phonetic()
