from flask import Flask, render_template, request
from requests import get

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    name = request.values["name"]
    pwd = request.values["pwd"]
    return f"<h1>Name: {name}\nPassword: {pwd}</h1>"


if __name__ == "__main__":
    app.run()
