from flask import Flask
from random import randint

NUMBER = randint(0, 9)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"<h1>Guess a number between 0 and 9!</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width='450'>"


@app.route("/<int:user_guess>")
def check_number(user_guess):
    if user_guess < NUMBER:
        return "<h1 style='color:red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='450'>"
    elif user_guess > NUMBER:
        return "<h1 style='color:blue'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='450'>"
    else:
        return "<h1 style='color:green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width='450'>"


if __name__ == "__main__":
    app.run(debug=True)
