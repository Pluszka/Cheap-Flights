from data_manager import DataManager
from flight_search import FlightSearch

flight = FlightSearch()
sheet_data = DataManager()

for country in sheet_data.prices:
    if len(country['iataCode']) == 0:
        country['iataCode'] = flight.get_code(country['city'])

for