from datetime import datetime
from requests import get, post

# ----------------------------- CONSTANTS --------------------------------------- #
# USER INFO
GENDER: str = "male/female"
WEIGHT_KG: int = 00
HEIGHT_CM: int = 00
AGE: int = 00

# MISC
TODAY = datetime.now().strftime("%d/%m/%Y,%I:%M:%S").split(",")
WORKOUT_SPREADSHEET_URL = "[URL FOR SPREADSSHEET"  # HAS TO BE GOOGLE SHEETS!!!

# SHEETY
SHEETY_URL = "[URL FOR SHEETY SHEET PROJECT]"
SHEETY_HEADERS = dict(Authorization="[IF YOU HAVE SECURITY]")

# NUTRIONIX
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = "[NUTRITIONIX APP ID]"
API_KEY = "[NUTRIONIX API KEY]"
EXERCISE_HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# ---------------------------- NUTRITIONIX -------------------------------------- #
exercise_params = {
    "query": input("What exercises have you done?\t"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=EXERCISE_HEADERS)
exercise_data = response.json()
exercises = exercise_data["exercises"]

for exercise in exercises:
    row_param = {
        "workout": {
            'date': TODAY[0],
            'time': TODAY[1],
            'exercise': exercise["name"].title(),
            'duration': round(exercise["duration_min"]),
            'calories': round(exercise["nf_calories"]),
        }
    }
    # ------------------------- SHEETY POST ------------------------------------- #
    response = post(url=SHEETY_URL, json=row_param, headers=SHEETY_HEADERS)
    print(response.text)

# ----------------------------- SHEETY GET -------------------------------------- #
response = get(url=SHEETY_URL, headers=SHEETY_HEADERS)
sheety_data = response.json()
print(sheety_data)
