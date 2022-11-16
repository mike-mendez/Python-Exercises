from flask import Flask, render_template
from datetime import datetime
from requests import get

CURRENT_YEAR = datetime.now().year
FIRST_NAME = "Mike"
FULL_NAME = "Mike Mendez"
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", fname=FIRST_NAME, year=CURRENT_YEAR, name=FULL_NAME)


@app.route("/guess/<string:name>")
def get_guesses(name):
    gender = get(url="https://api.genderize.io/", params={'name': name}).json()["gender"]
    age = get(url="https://api.agify.io/", params={'name': name}).json()["age"]
    country_id = get(url="https://api.nationalize.io/", params={'name': name}).json()["country"][0]["country_id"]
    country_name = get(url=f"https://restcountries.com/v3.1/alpha/{country_id}").json()[0]["name"]["common"]

    return render_template("guess.html", name=name.title(), gender=gender, age=age, country=country_name)


if __name__ == "__main__":
    app.run(debug=True)
