from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

GOOGLE_SHEET = "https://docs.google.com/spreadsheets/d/1EmtXpWtfUnvv4QB4Oww676TQTwUAgYr2Bt2xLYgbnZ0/edit#gid=0"

data = DataManager()
search = FlightSearch()
flight = FlightData()
notification = NotificationManager()

sheet_data = data.get_data()



# for i in sheet_data:
#     i['iataCode'] = (search.iata_check(i)) #print(sheet_data[0]['city'])
#
# for i in sheet_data:
#     data.put(i)

# for i in sheet_data:
#     i['iataCode'] = search.iata_check(i)
#
# pprint(sheet_data)
#
# for i in sheet_data:
#     data.put(i)



for i in sheet_data:
    flight_data = flight.flight_get(i)

    flight_price = flight_data['data'][0]['price']
    sheet_price = i['lowestPrice']

    flight_from_city = flight_data['data'][0]['cityCodeFrom']
    flight_from_airport = flight_data['data'][0]['flyFrom']

    flight_to_city = flight_data['data'][0]['cityCodeTo']
    flight_to_airport = flight_data['data'][0]['flyTo']

    flight_route = flight_data['data'][0]['route']
    flight_outbound_date = flight_route[0]['local_departure'].split('T')[0]
    flight_inbound_date = flight_route[len(flight_route)-1]['local_departure'].split('T')[0]

    if flight_price < sheet_price:
        print(f"{flight_to_city}-{flight_to_airport} : {flight_price} ### {sheet_price}")
        notification.texting(f"""
            # Price
            {flight_price}\n
            # Departure City Name
            {flight_from_city}\n
            # Departure Airport IATA Code
            {flight_from_airport}\n
            # Arrival City Name
            {flight_to_city}\n
            # Arrival Airport IATA Code
            {flight_to_airport}\n
            # Outbound Date
            {flight_outbound_date}\n
            # Inbound Date       
            {flight_inbound_date} 
        """)
    # print(f"{flight_to_airport} : {flight_outbound_date} - {flight_inbound_date}")



# flight_route = flight.flight_get(sheet_data[1])['data'][0]['route']
# print(flight_route[0]['local_departure'].split('T')[0])
# print(flight_route[len(flight_route)-1]['local_departure'].split('T')[0])
