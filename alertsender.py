import pandas as pd
import smtplib

class AlertSender():
    def __init__(self):
        #Demands config and email sending config

        #Set your demand price as float
        DEMAND_PRICE = ""
        self.Price_to_save = 0
        self.Time_to_save = ''
        self.Date_to_save = ''


        data_to_read = pd.read_csv("BITCOINPRICES.csv", sep=';')
        x = 0
        for n in data_to_read['Price']:
            if n < DEMAND_PRICE:
                self.Price_to_save = n
                self.Time_to_save = data_to_read['Time'][x]
                self.Date_to_save = data_to_read['Day'][x]
            x =+ 1

        with smtplib.SMTP_SSL("smtp.gmail.com",port=465) as mail:
            user = 'your email on gmail'
            password = 'your password to email'
            receiver = 'receiver email'

            mail.login(user=user,password=password)
            msg = f"Subject:ALERT!!!\nBitcoin price fulfilled your demands and his price reached {self.Price_to_save} USD," \
                  f"at {self.Time_to_save}, {self.Date_to_save}."

            mail.sendmail(f'{user}',f'{receiver}', msg=msg)