import requests
import datetime as dt

#Class to downloand data from API

class CatchData():
    def __init__(self):
        #Saving data
        self.data = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy").json()['data']['amount']
        self.day = dt.datetime.now().strftime("%d %b %Y")
        self.time = dt.datetime.now().strftime("%H:%M")