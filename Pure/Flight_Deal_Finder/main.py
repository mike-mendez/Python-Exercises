from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

from datetime import datetime
from dateutil.relativedelta import relativedelta
from json import dumps

# ------------------------------ CONSTANTS ---------------------------------- #
DEPARTING_CITY = "[IATA CODE]"
MIN_NIGHTS = 00  # MIN NIGHTS
MAX_NIGHTS = 00  # MAX NIGHTS

# -------------------------- GETTING IATA CODES ----------------------------- #
# GETTING CITIES FROM SPREADSHEET WITH SHEETY
cities = DataManager().get_cities()

# GET DATA FROM TEQUILA
iata_codes = FlightSearch(cities).find_iata_codes()

# UPDATE ROWS WITH IATA CODE
update_rows_iata = DataManager().update_row_iata(iata_codes)

# # -------------------------- SEARCHING FLIGHTS ------------------------------ #
flight_iata_codes = DataManager().get_iata_price()

tomorrow = datetime.now() + relativedelta(days=+1)
six_months = tomorrow + relativedelta(months=+6)

search_flights = FlightSearch(flight_iata_codes).search_flights(departing_iata=DEPARTING_CITY,
                                                                data_from=tomorrow.strftime("%d/%m/%Y"),
                                                                date_to=six_months.strftime("%d/%m/%Y"),
                                                                min_nights=MIN_NIGHTS,
                                                                max_nights=MAX_NIGHTS)

# ------------------------ SENDING DEALS VIA SMS ---------------------------- #
flight_deals = FlightData(search_flights) if len(search_flights) > 0 else False
if flight_deals:
    with open("flight_deals.json", "w") as deals:
        deals.write(dumps(search_flights, indent=4))
    flight_deals = flight_deals.sms_format()

    sms_msgs = NotificationManager(flight_deals)
    sms_msgs = sms_msgs.send_msgs()
else:
    print("No deals were found")

