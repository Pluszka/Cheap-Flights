import os
import requests

ENDPOINT_KIWI = 'https://tequila-api.kiwi.com/locations/query'

header = {
    'apikey': os.environ.get('KIWI_API_KEY')
}

class FlightSearch:
    def get_code(self, city):
        query = {
            'term': city,
            'location_types': 'city'
        }
        response = requests.get(url=ENDPOINT_KIWI, params=query, headers=header)
        response.raise_for_status()
        code = response.json()['locations'][0]['code']
        return code
