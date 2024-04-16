from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data = DataManager()
price_sheet_data = data.price_gsheet_data['prices']
user_sheet_data = data.user_gsheet_data['users']
#print(sheet_data)

## Update IATA code
# for i in range(len(price_sheet_data)):
#     location = price_sheet_data[i]['city']
#     row_id = str(price_sheet_data[i]['id'])
#     iata = flightSearch.query_IATA(location)
#     price_sheet_data[i]['iataCode'] = iata
#     data.update_gsheet("iataCode", iata)
#
# pprint(sheet_data)


for i in range(len(price_sheet_data)):
    loc = price_sheet_data[i]['iataCode']
    lowestPrice = price_sheet_data[i]['lowestPrice']
    flightsearch = FlightSearch(loc)
    minPriceDetail = flightsearch.get_lowest_price()
    try:
        if minPriceDetail['price'] < lowestPrice:
            msg = (f'Low Price Alert! Only ${minPriceDetail['price']} '
                   f'to fly from {minPriceDetail['departure_flyFrom']} '
                   f'to {minPriceDetail['departure_flyTo']}, '
                   f'from {minPriceDetail['departure_departureTime'].split("T")[0]} '
                   f'to {minPriceDetail['return_arrivalTime'].split("T")[0]}.\n')
            if flightsearch.stopovers == 1:
                msg += f'Flight has 1 stopover, via {minPriceDetail['stopover']}'
            notify = NotificationManager()
            notify.send_msg(msg)

            for i in range(len(user_sheet_data)):
                to_email = user_sheet_data[i]['email']
                first_name = user_sheet_data[i]['firstName']
                last_name = user_sheet_data[i]['lastName']
                notify.send_email(to_email, first_name, last_name, msg)
    except:
        pass
