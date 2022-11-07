from datetime import datetime
from requests import post, put, delete

# ----------------------------- CONSTANTS --------------------------------------- #
USERNAME = "[YOUR_USERNAME]"
TOKEN = "[YOUR_PASSWORD]"
GRAPH_ID = "[YOUR_GRAPH_ID]"
DATE = date = datetime.now().strftime("%Y%m%d")  # yyyyMMdd
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
UPDATE_GRAPH_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
UPDATE_PIXEL_ENDPOINT = f"{UPDATE_GRAPH_ENDPOINT}/"
HEADER = {
    "X-USER-TOKEN": TOKEN,
}

# ---------------------------- CREATE USER -------------------------------------- #
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)

# --------------------------- CREATE GRAPH -------------------------------------- #
graph_config = {
    "id": "steps-taken",
    "name": "Steps Taken",
    "unit": "steps",
    "type": "int",
    "color": "sora",
}

response = post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADER)
print(response.text)

# --------------------------- UPDATE GRAPH -------------------------------------- #
# IGNORE FOR UTC
update_config = {
    "timezone": "TZ DATABASE NAME"
}

response = put(url=UPDATE_GRAPH_ENDPOINT, json=update_config, headers=HEADER)
print(response.text)

# ---------------------------- POST PIXEL --------------------------------------- #
pixel_config = dict(date=DATE, quantity=input("Enter amount of steps taken today:\t"))

response = post(url=UPDATE_GRAPH_ENDPOINT, json=pixel_config, headers=HEADER)
print(response.text)

# --------------------------- UPDATE PIXEL -------------------------------------- #
pixel_config = dict(date=DATE, quantity=input("Enter the updated step amount:\t"))

response = put(url=UPDATE_PIXEL_ENDPOINT, json=pixel_config, headers=HEADER)
print(response.text)

# --------------------------- DELETE PIXEL -------------------------------------- #
response = delete(url=UPDATE_PIXEL_ENDPOINT, headers=HEADER)
print(response.text)
