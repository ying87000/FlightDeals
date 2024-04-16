import requests


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.price_api = "https://api.sheety.co/46eaace6c0923e882fbe2f5e8f3bf9bc/flightDeals/prices"
        self.user_api = "https://api.sheety.co/46eaace6c0923e882fbe2f5e8f3bf9bc/flightDeals/users"
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





