import requests
from datetime import datetime, timedelta
from pprint import pprint

FROM_DATE = (datetime.today() + timedelta(days=7)).strftime("%d/%m/%Y")
TO_DATE = (datetime.today() + timedelta(days=14)).strftime("%d/%m/%Y")


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""

    def __init__(self, location):
        self.location = location
        self.apikey = {"apikey": "NlN_vm5LU1YwKRfwhLq_45D4cWg9sLZe"}
        self.locationEndpoint = "https://api.tequila.kiwi.com/locations/query"
        self.searchEndpoint = "https://api.tequila.kiwi.com/v2/search"
        self.locationParameter = None
        self.search_para = None
        self.stopovers = 0
        self.flight_data = None
        self.price_list = []
        self.stopover_search_para={}

    def query_IATA(self):
        self.locationParameter = {
            "term": self.location
        }
        iata_response = requests.get(url=self.locationEndpoint, headers=self.apikey, params=self.locationParameter)
        return iata_response.json()['locations'][0]['code']

    def get_flight_data(self):
        self.search_para = {
            "fly_from": "TPE",
            "fly_to": self.location,
            "date_from": FROM_DATE,
            "date_to": TO_DATE,
            "max_stopovers": 0,  # Direct flight
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,  # Round trip between 7 - 28 days
            "curr": "TWD",
        }

        response = requests.get(url=self.searchEndpoint, headers=self.apikey, params=self.search_para)
        response.raise_for_status()
        if response.json()['_results'] > 0:
            pass
        else:
            self.stopovers = 1
            print(f"Now change {self.location} maximum stopover to one")
            self.stopover_search_para = {
                "fly_from": "TPE",
                "fly_to": self.location,
                "date_from": FROM_DATE,
                "date_to": TO_DATE,
                "max_sector_stopovers": 1,  # Change Stopovers
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,  # Round trip between 7 - 28 days
                "curr": "TWD",
            }
            response = requests.get(url=self.searchEndpoint, headers=self.apikey, params=self.stopover_search_para)

        return response.json()

    def get_flight_price(self):
        self.flight_data = self.get_flight_data()
        try:
            for i in range(len(self.flight_data['data'])):
                self.price_list.append(
                    {
                        #'id': self.flight_data['data'][i]['route'][0]['combination_id'],
                        'price': self.flight_data['data'][i]['price'],
                        #'departure_cityFrom': self.flight_data['data'][i]['route'][0]['cityFrom'],
                        'departure_flyFrom': self.flight_data['data'][i]['route'][0]['flyFrom'],
                        'departure_departureTime': self.flight_data['data'][i]['route'][0]['local_departure'],
                        #'departure_cityTo': self.flight_data['data'][i]['route'][0]['cityTo'],
                        'departure_flyTo': self.location,
                        'return_arrivalTime': self.flight_data['data'][i]['route'][-1]['local_arrival'],
                        'stopover': self.flight_data['data'][i]['route'][0]['cityTo']
                    }
                )

        finally:
            return self.price_list

    def get_lowest_price(self):
        try:
            self.price_list = self.get_flight_price()
            minPricedItem = min(self.price_list, key=lambda x: x['price'])
            # print(f"{location}: {minPricedItem['price']}")
            return minPricedItem
        except:
            return "None"
