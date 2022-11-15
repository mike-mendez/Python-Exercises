from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def make_bold(func):
    def wrapper():
        text = func()
        return f"<b>{func()}</b>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        text = func()
        return f"<em>{func()}</em>"
    return wrapper


def make_underline(func):
    def wrapper():
        text = func()
        return f"<u>{func()}</u>"
    return wrapper


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
