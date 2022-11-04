import requests
from datetime import datetime

MY_LAT = 37.526371
MY_LNG = 126.896225

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_hr = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hr = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise_hr)
print(sunset_hr)

time_now = datetime.now()
print(time_now.hour)