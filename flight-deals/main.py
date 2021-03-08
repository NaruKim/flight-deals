from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

data = DataManager()
search = FlightSearch()

sheet_data = data.get_data()
# print(sheet_data[0]['city'])

search.iata_check(sheet_data[1])

for i in sheet_data:
    print(search.iata_check(i))