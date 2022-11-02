from tkinter import *
from random import choice
from pandas import DataFrame, read_csv

# ----------------------------- CONSTANTS --------------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "Spanish"
COUNTDOWN = 3000

# --------------------------- LANGUAGE DATA ------------------------------------- #
try:
    data = read_csv(f"data/{LANGUAGE.lower()}_words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = read_csv(f"data/{LANGUAGE.lower()}_words.csv").to_dict(orient="records")
finally:
    current_card = {}


# --------------------------- GET RANDOM WORD ----------------------------------- #
def next_card():
    global current_card, flip_countdown
    window.after_cancel(flip_countdown)
    current_card = choice(data)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_language, text=LANGUAGE, fill="black")
    canvas.itemconfig(card_word, text=current_card[LANGUAGE], fill="black")
    flip_countdown = window.after(COUNTDOWN, func=flip_card)


# ----------------------------- FLIP CARD --------------------------------------- #
def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_language, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ----------------------------- WORD KNOWN -------------------------------------- #
def word_known():
    data.remove(current_card)
    word_list = DataFrame(data)
    word_list.to_csv(f"data/{LANGUAGE.lower()}_words_to_learn.csv", index=False)
    next_card()


# ------------------------------ UI SETUP --------------------------------------- #

# WINDOW
window = Tk()
window.title(f"My Anki Card App | Learning {LANGUAGE}")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_countdown = window.after(COUNTDOWN, func=flip_card)

# CARD FRONT
card_front_img = PhotoImage(file="./images/card_front.png")

# CARD BACK
card_back_img = PhotoImage(file="./images/card_back.png")

# CANVAS
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, columnspan=2, row=0)

# CARD TEXT
card_language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), justify="center")

# WRONG BUTTON
wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

# RIGHT BUTTON
right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=word_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
