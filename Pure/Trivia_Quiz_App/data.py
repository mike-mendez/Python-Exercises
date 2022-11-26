from requests import get

QUESTION_AMOUNT = 10
CATEGORY = None
DIFFICULTY = None
QUESTION_TYPE = "boolean"  # or "multiple" for MC

parameters = {
    "amount": QUESTION_AMOUNT,
    "category": CATEGORY,
    "difficulty": DIFFICULTY,
    "type": QUESTION_TYPE,
}

response = get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]
