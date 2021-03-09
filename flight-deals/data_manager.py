import requests
from pprint import pprint

GET_ENDPOINT = "https://api.sheety.co/8aee92b9d053a6a4c35116f530584a6f/copyOfFlightDeals/prices"
POST_ENDPOINT = "https://api.sheety.co/8aee92b9d053a6a4c35116f530584a6f/copyOfFlightDeals/prices"
PUT_ENDPOINT = "https://api.sheety.co/8aee92b9d053a6a4c35116f530584a6f/copyOfFlightDeals/prices" #/[Object ID]
DELETE_ENDPOINT = "https://api.sheety.co/8aee92b9d053a6a4c35116f530584a6f/copyOfFlightDeals/prices" #/[Object ID]


class DataManager:
    def __init__(self):
        pass

    def get(self):
        get_response = requests.get(GET_ENDPOINT)
        return get_response.json()

    def get_data(self):
        json_data = self.get()
        return json_data['prices']

    def put(self, n):
        id = n['id']
        put_json = {
            "price": {
                "city": n['city'],
                "iataCode": n["iataCode"],
                "lowestPrice": n["lowestPrice"]
        }
        }
        put_response = requests.put(f"{PUT_ENDPOINT}/{id}", json=put_json)
        print(put_response)