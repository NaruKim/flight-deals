import requests
from pprint import pprint

GET_ENDPOINT = "https://api.sheety.co/ca700cff5747162c513bf4821d202b1a/flightDeals/prices"
POST_ENDPOINT = "https://api.sheety.co/ca700cff5747162c513bf4821d202b1a/flightDeals/prices"
PUT_ENDPOINT = "https://api.sheety.co/ca700cff5747162c513bf4821d202b1a/flightDeals/prices" #/[Object ID]
DELETE_ENDPOINT = "https://api.sheety.co/ca700cff5747162c513bf4821d202b1a/flightDeals/prices" #/[Object ID]


class DataManager:
    def __init__(self):
        pass

    def get(self):
        get_response = requests.get(GET_ENDPOINT)
        return get_response.json()

    def get_data(self):
        json_data = self.get()
        return json_data['prices']


pilot = DataManager()
n = pilot.get_data()