from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

data = DataManager()
search = FlightSearch()

sheet_data = data.get_data()

for i in sheet_data:
    i['iataCode'] = (search.iata_check(i)) #print(sheet_data[0]['city'])



pprint(sheet_data[0]['id'])