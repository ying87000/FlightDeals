import requests

### Create a google sheet named "Flight Deals", which contains two tab: prices and users ###
### Get API for both tabs on Sheety ###
PRICE_API = ""
USER_API = ""

class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.price_api = PRICE_API
        self.user_api = USER_API
        self.price_gsheet_data = requests.get(self.price_api).json()
        self.user_gsheet_data = requests.get(self.user_api).json()

    def update_gsheet(self, rowid, column, content):
        new_api = f"{self.price_api}/{rowid}"
        update_data = {
            'price': {
                column: content}
        }
        response = requests.put(new_api, json=update_data)
        response.raise_for_status()





