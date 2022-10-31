import random
import re

RPS = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}


def ascii_rps(choice):
    match choice:
        case "0":
            print("""
                    _______
                ---'   ____)
                      (_____)
                      (_____)
                      (____)
                ---.__(___)
                """)
        case "1":
            print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)
        case "2":
            print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)


while True:
    player_choice = input("Choose your weapon (0 - Rock | 1 - Paper | 2 - Scissor:\t")
    if re.search('[012]', player_choice):
        break
    else:
        print("Your input was invalid. Please try again.")

print(f"You have chosen {RPS[player_choice]}")
ascii_rps(player_choice)

computer_choice = str(random.randint(0, 2))
print(f"Computer has chosen {RPS[computer_choice]}")
ascii_rps(computer_choice)

match player_choice:
    case "0":
        if computer_choice == "1":
            print("You lose :(")
        elif computer_choice == "2":
            print("You win!!!")
        else:
            print("It's a tie")
    case "1":
        if computer_choice == "2":
            print("You lose :(")
        elif computer_choice == "0":
            print("You win!!!")
        else:
            print("It's a tie")
    case "2":
        if computer_choice == "0":
            print("You lose :(")
        elif computer_choice == "1":
            print("You win!!!")
        else:
            print("It's a tie")