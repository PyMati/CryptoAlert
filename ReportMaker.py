import pandas as pd
from data import CatchData

class MakeCSVReport():
    def __init__(self):
        #Accesing information from API
        obj = CatchData()
        time = obj.time
        day = obj.day
        data = obj.data

        self.data_to_save = {f"Time": [time],
                        f"Day": [day],
                        f"Price": [data]}


        try:
            read_data = pd.read_csv("BITCOINPRICES.csv")
            print('New data saved')
            self.data_add(self.data_to_save)
        except:
            print("Creating file...")
            create_csv = pd.DataFrame(self.data_to_save).to_csv("BITCOINPRICES.csv", sep=";")

    def data_add(self,info):

        new_row = pd.DataFrame(info)
        new_row.to_csv("BITCOINPRICES.csv", mode = 'a',header=False, sep=";")



