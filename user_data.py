import os
import requests

ENDPOINT = f"{os.environ.get('API_PRICES&USERS')}/users"

header = {
    'Authorization': f'Bearer {os.environ.get("TOKEN-FC")}'
}


class UserData:

    def __init__(self):
        self.users = {}
        self.get_users()

    def get_users(self):
        response = requests.get(url=ENDPOINT, headers=header)
        response.raise_for_status()
        data = response.json()
        print(data)
        self.users = data['users']

    def add_user(self):
        new_params = {
        'user': {
            'firstName': input('Enter your first name:'),
            'lastName': input('Enter your last name:'),
            'email': input('Enter your email:')
            }
        }
        response = requests.put(url=f'{ENDPOINT}/{len(self.users)+2}', json=new_params, headers=header)
        print(response.text)
