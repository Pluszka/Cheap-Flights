import os
import requests
from pprint import pprint

ENDPOINT = os.environ.get('FLIGHTS_SHEET_API')

header = {
    'Authorization': f'Bearer {os.environ.get("TOKEN_FLIGHTS_SHEET")}'
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass