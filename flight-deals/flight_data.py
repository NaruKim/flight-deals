import requests
from pprint import pprint
from datetime import datetime
from dateutil.relativedelta import relativedelta

TEQUILA_API_KEY = "EOs6dLXx_gMjQmfccmTCUvCKxwh2rsiE"
TEQUILA_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"


now = datetime.now()
today = now.strftime("%d/%m/%Y")
six_months_later = (now + relativedelta(months=+6)).strftime("%d/%m/%Y")



class FlightData:
    def flight_get(self, n):
        headers = {
            "apikey" : TEQUILA_API_KEY,
        }
        query = {
            "fly_from":"LON",
            "fly_to":n['iataCode'],
            "date_from":today,
            "date_to":six_months_later,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type":"round",
            "one_for_city": 1,
            "max_stopobers": 0,
            "curr":"GBP",
        }
        response = requests.get(url=TEQUILA_SEARCH_ENDPOINT, params=query, headers=headers)
        return response.json()