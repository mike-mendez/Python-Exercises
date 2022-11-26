from requests import get

API_KEY = "[YOUR KIWI API KEY]"
ENDPOINT = "https://api.tequila.kiwi.com"
LOCATIONS_ENDPOINT = f"{ENDPOINT}/locations/query"
SEARCH_ENDPOINT = f"{ENDPOINT}/v2/search"
HEADERS = dict(accept="application/json", apikey=API_KEY)


class FlightSearch:
    def __init__(self, data):
        self.data = data

    def find_iata_codes(self):
        iata_codes = []
        for city in self.data:
            location_params = {
                "term": f"{city}",
                "location_type": "city",
                "limit": 1,
            }
            response = get(url=LOCATIONS_ENDPOINT, params=location_params, headers=HEADERS)
            results = response.json()
            iata_code = results["locations"][0]["code"]
            iata_codes.append(iata_code)
        return iata_codes

    def search_flights(self, departing_iata, data_from, date_to, min_nights, max_nights):
        flight_deals = []
        for dest_data in self.data:
            search_params = {
                "fly_from": departing_iata,
                "fly_to": dest_data["iataCode"],
                "date_from": data_from,
                "date_to": date_to,
                "nights_in_dst_from": min_nights,
                "nights_in_dst_to": max_nights,
                "flight_type": "round",
                "curr": "USD",  # CAN INPUT OTHER CURRENCIES
                "locale": "en",  # CAN INPUT OTHER LANGUAGES
                "price_to": dest_data["lowestPrice"],
                "limit": 1,
            }
            response = get(url=SEARCH_ENDPOINT, params=search_params, headers=HEADERS)
            results = response.json()
            flight_deals.append(results) if len(results["data"]) else None
        print(f"Found {len(flight_deals)} deals!")
        return flight_deals
