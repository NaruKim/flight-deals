import requests
from pprint import pprint

TEQUILA_API_KEY = "EOs6dLXx_gMjQmfccmTCUvCKxwh2rsiE"
TEQUILA_QUERY = "https://tequila-api.kiwi.com/locations/query"



class FlightSearch:
    def __init__(self):
        pass

    def iata_check(self, n):
        query = {
            "term": n['city'],
            "location_types": "city"
        }
        headers = {
            "apikey": TEQUILA_API_KEY,
        }
        response = requests.get(TEQUILA_QUERY, params=query, headers=headers)
        return (response.json()['locations'][0]['code'])
