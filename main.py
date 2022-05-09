import time
from data import CatchData
from ReportMaker import MakeCSVReport
from alertsender import AlertSender
import datetime as dt

minutes_passed = dt.timedelta(minutes=30)
start = dt.datetime.now()
end = start + minutes_passed

while True:
    time.sleep(2)
    CatchData()
    MakeCSVReport()
    # If 30 minutes have passed, send e-mail
    if end==dt.datetime.now():
        start = dt.datetime.now()
        end = start + minutes_passed
        AlertSender()