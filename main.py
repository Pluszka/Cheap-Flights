from data_manager import DataManager
from flight_search import FlightSearch

flight = FlightSearch()
sheet_data = DataManager()
print(sheet_data.prices)

for country in sheet_data.prices:
    if len(country['iataCode']) == 0:
        country['iataCode'] = flight.get_code(country['city'])
        # sheet_data.update_IATA(country)
print(sheet_data.prices)