from datetime import datetime
from requests import get
from smtplib import SMTP
from time import sleep

# ----------------------------- LAT/LNG DATA --------------------------------------- #
MY_LAT = 37.526371
MY_LNG = 126.896225

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


def is_iss_overhead():
    # --------------------------- ISS LOCATION API --------------------------------- #
    response = get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG + 5:
        return True


def is_night():
    # ------------------------- SUNRISE/SUNSET API ---------------------------------- #
    response = get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    ss_data = response.json()
    sunrise_hr = int(ss_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hr = int(ss_data["results"]["sunset"].split("T")[1].split(":")[0])

    # ----------------------------- CURRENT TIME ------------------------------------ #
    hour_now = datetime.now().hour

    if sunset_hr <= hour_now <= sunrise_hr:
        return True


# ----------------------------- CONDITIONALS ----------------------------------- #

while True:
    sleep(60)
    if is_iss_overhead() and is_night():
        # ---------------------- EMAIL MSG ------------------------------------- #
        email = "sending@gmail.com"
        password = "password"
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Encrypts sent email if read by an interceptor
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs="receiving@gmail.com",
                msg="Subject:Look Up \n\nThe ISS is above you!"
            )
