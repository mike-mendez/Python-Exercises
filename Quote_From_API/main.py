from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.quotable.io/random")
    response.raise_for_status()
    quote = response.json()["content"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Dude Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="./images/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Dude Says...", width=250, font=("Arial", 20, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

dude_img = PhotoImage(file="./images/dude.png")
dude_button = Button(image=dude_img, highlightthickness=0, command=get_quote)
dude_button.grid(row=1, column=0)

window.mainloop()
