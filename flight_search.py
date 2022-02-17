import os
import requests
import datetime as dt

from flight_data import FlightData

ENDPOINT_KIWI = 'https://tequila-api.kiwi.com'
header = {
    'apikey': os.environ.get('KIWI_API_KEY')
}
MY_LOCATION = 'WAW'
tomorrow = dt.date.today() + dt.timedelta(1)
end_of_searching = dt.date.today() + dt.timedelta(180)


class FlightSearch:
    def get_code(self, city):
        query = {
            'term': city,
            'location_types': 'city'
        }
        response = requests.get(url=f'{ENDPOINT_KIWI}/locations/query', params=query, headers=header)
        response.raise_for_status()
        code = response.json()['locations'][0]['code']
        return code

    def found_flight(self, city_code):
        query = {
            'fly_from ': MY_LOCATION,
            'fly_to': city_code,
            'date_from ': tomorrow.strftime("%d/%m/%Y"),
            'date_to ': end_of_searching.strftime("%d/%m/%Y"),
            'flight_type': 'round',
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=f'{ENDPOINT_KIWI}/v2/search', params=query, headers=header)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f'No flights founded to {city_code}')
            return None
        offer = FlightData(data["price"], data["route"][0]["cityFrom"],
                data["route"][0]["flyFrom"], data["route"][0]["cityTo"],
                data["route"][0]["flyTo"], data["route"][0]["local_departure"].split("T")[0],
                data["route"][1]["local_departure"].split("T")[0])
        return offer
