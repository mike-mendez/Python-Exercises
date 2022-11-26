from requests import get, put

ENDPOINT = "https://api.sheety.co/USER_ID/flightDealFinder/prices"
HEADERS = dict(Authorization="[YOUR AUTHORIZATION]")


class DataManager:
    def __init__(self):
        self.response = None

    def get_cities(self):
        self.response = get(url=ENDPOINT, headers=HEADERS)
        data = self.response.json()

        cities = []
        for row in data["prices"]:
            cities.append(row["city"])
        return cities

    def get_iata_price(self):
        self.response = get(url=ENDPOINT, headers=HEADERS)
        data = self.response.json()

        iata_codes = []
        for row in data["prices"]:
            iata_codes.append(dict(iataCode=row["iataCode"], lowestPrice=row["lowestPrice"]))
        return iata_codes

    def update_row_iata(self, data):
        for row in range(len(data)):
            row_params = {
                "price": {
                    "iataCode": data[row],
                }
            }
            self.response = put(url=f"{ENDPOINT}/{row + 2}", json=row_params, headers=HEADERS)
