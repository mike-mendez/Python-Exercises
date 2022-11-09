from json import dumps
from random import getrandbits
from requests import get

CUTTLY_API_KEY = "[YOUR CUTTLY API KEY]"
CUTTLY_ENDPOINT = "http://cutt.ly/api/api.php"


class FlightData:
    def __init__(self, data):
        self.data = data

    def shorten_url(self, url: str) -> str:
        hash = "%08x" % getrandbits(32)
        name = hash
        cuttly_params = {
            "key": CUTTLY_API_KEY,
            "short": url,
            "name": name,
        }
        response = get(url=CUTTLY_ENDPOINT, params=cuttly_params)
        data = response.json()
        return data["url"]["shortLink"]

    def sms_format(self):
        sms_bodies = []
        for flight in self.data:
            itinerary = flight["data"][0]
            price = itinerary["price"]
            dep_city = itinerary["cityFrom"]
            dep_airport = itinerary["flyFrom"]
            arr_city = itinerary["cityTo"]
            arr_airport = itinerary["flyTo"]
            from_date = itinerary["route"][0]["local_departure"].split("T")[0]
            to_date = itinerary["route"][-1]["local_departure"].split("T")[0]
            url = self.shorten_url(itinerary["deep_link"])
            sms_body = f"Low Price Alert! Only ${price} to fly from {dep_city}-{dep_airport}" \
                       f" to {arr_city}-{arr_airport}\n" \
                       f"From: {from_date}\n" \
                       f"To:   {to_date}\n" \
                       f"Link: {url}"
            sms_bodies.append(sms_body)
        return sms_bodies
