from os import environ
from requests import get
from twilio.rest import Client

# ------------------------------ CONSTANTS ------------------------------------- #
OMW_FORECAST_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"
API_KEY = "[YOUR_API_KEY]"  # FOR OMW
CITY_TOWN = "[CITY]"
COUNTRY_CODE = "[COUNTRY_CODE]"  # LOWERCASE; TWO LETTERS
TEMP_UNIT = "[UNIT["
TWILLIO_NUM = "[YOUR_TWILIO_NUMBER"
RECEIVING_NUM = "[RECEIVING_NUMBER]"

# ------------------------------- TWILIO DATA ---------------------------------- #
account_sid = environ['TWILIO_ACCOUNT_SID'] = "[YOUR_TWILIO_ACCOUNT_SID]"
auth_token = environ['TWILIO_AUTH_TOKEN'] = "[YOUR_TWILIO_AUTH_TOKEN]"
client = Client(account_sid, auth_token)

# ------------------------------ DATA PARAMETERS ------------------------------- #
parameters_city = {
    "q": f"{CITY_TOWN},{COUNTRY_CODE}",
    "appid": API_KEY,
    "units": TEMP_UNIT,
    "cnt": "[OPTIONAL]"  # TAKES AN INT
}

# ----------------------------------- OMW API --------------------------------- #
response_weather = get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters_city)
response_weather.raise_for_status()
forecast_data = response_weather.json()
will_rain = False

for third_hour in forecast_data["list"]:
    condition_code = third_hour["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
        break

# --------------------------------- TWILIO SMS ------------------------------- #
if will_rain:
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring a umbrella ☂️",
        from_=TWILLIO_NUM,
        to=RECEIVING_NUM,
    )
    print(message.status)
