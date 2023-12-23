# import [module] 
# import [module] as newname
# from [module] import *
# get datetime from py-module
import requests
import datetime

# data from Kraken.API 
resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
print(resp)
print(resp.json())

# show datetime
resp = datetime.datetime.now()
# show time now
print("Time for now:", resp)
# show time before 5hours and 30mins
print("Before 5hours and 30mins: ", resp - datetime.timedelta(hours=5, minutes=30))
# show time after 3days and before 3days
print("After 3days: ", resp + datetime.timedelta(days=3))
print("Before 3days: ", resp - datetime.timedelta(days=3))


