import os
import requests

ENDPOINT = f"{os.environ.get('API_PRICES&USERS')}/prices"

header = {
    'Authorization': f'Bearer {os.environ.get("TOKEN-FC")}'
}


class DataManager:
    def __init__(self):
        self.prices = {}
        self.get_prices()

    def get_prices(self):
        response = requests.get(url=ENDPOINT, headers=header)
        response.raise_for_status()
        data = response.json()
        self.prices = data['prices']

    def update_IATA(self, country):
        params_to_update = {
            'price': {
                'iataCode': country['iataCode']
            }
        }
        response = requests.put(url=f'{ENDPOINT}/{country["id"]}', json=params_to_update, headers=header)
        print(response.text)