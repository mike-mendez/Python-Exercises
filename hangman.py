import random
import string

word_bank = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
             'coyote crow deer dog donkey duck eagle ferret fox frog goat '
             'goose hawk lion lizard llama mole monkey moose mouse mule newt '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra ').split()

HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
""")

# INITIALIZED VARIABLES
guessed_letters = []
guesses = 0
chosen_word = word_bank[random.randrange(len(word_bank))]
current_word = ""
for letter in chosen_word:
    current_word += "_"


# FUNCTIONS
def find_occurrences(string, ch):
    return [s for s, ltr in enumerate(string) if ltr == ch]


while current_word != chosen_word and guesses != 6:
    player_guess = input("Guess a letter:\t")

    if string.ascii_letters.find(player_guess) == -1:
        print("Please type in letters only!")
    else:
        if player_guess in guessed_letters:
            print(f"You've already guessed {player_guess}. Try a different letter")
        else:
            guessed_letters.append(player_guess)
            if player_guess not in chosen_word:
                guesses += 1
                print(f"Letters guessed:\t{guessed_letters}")
                displayed_word = ""
                for i in range(len(current_word)):
                    displayed_word += f"{current_word[i]} "
                print(displayed_word)
                print(f"You guessed {player_guess}. That's not in the word. You lose a life.")
            else:
                guesses += 1
                ltr_ind = find_occurrences(chosen_word, player_guess)
                updated_word = ""
                for i in range(len(chosen_word)):
                    if string.ascii_letters.find(current_word[i]) != -1:
                        updated_word += current_word[i]
                    else:
                        if chosen_word[i] == player_guess:
                            updated_word += chosen_word[i]
                        else:
                            updated_word += current_word[i]
                current_word = updated_word
                displayed_word = ""
                for i in range(len(current_word)):
                    displayed_word += f"{current_word[i]} "
                print(f"Letters guessed:\t{guessed_letters}")
                print(displayed_word)
                print(f"You guessed {player_guess}. That's in the secret word!.")
    print(HANGMAN_PICS[guesses])

if guesses == 6:
    print(HANGMAN_PICS[guesses])
    print(f"You have been hanged :(\nThe word was {chosen_word}")
else:
    print(f"You have won, congrats!\nYou got it in {guesses} guesses.")
