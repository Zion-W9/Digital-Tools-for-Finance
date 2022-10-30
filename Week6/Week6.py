import requests
import datetime
import json
import pandas as pd
import time

# 1 The first part is about the Binance API:
# 1.1 What is the root URL?
print("https://api.binance.com")

# 1.2 What is the endpoint to retrieve klines (open-high-low-close data) for a specific cryptocurrency?
print('/api/v3/klines')

# 1.3 Specify a request string to retrieve 75 observations of klines data for BTCUSDT since 2022-09-01.
def retrieves_data(currency, date):
    date = int(time.mktime(datetime.datetime.strptime(date, '%d/%m/%Y').timetuple()))
    req = "{root_url}/{endpoint}?symbol={symbol}&interval={interval}&startTime={startTime}&limit={limit}" \
        .format(root_url="https://api.binance.com",
                endpoint='api/v3/klines',
                symbol=currency,
                interval="1m",
                limit='75',
                startTime=date)
    print(req)
    resp = requests.get(req)
    print(resp)

    #convert to DataFrame
    data = pd.DataFrame.from_records(
        resp.json(),
        columns=["Time", "Open", "High", "Low", "/","/",'/','/','/','/','/','/']
    )
    data.index = data.pop("Time").map(lambda x: datetime.datetime.fromtimestamp(x/1000))
    print(data)

retrieves_data("BTCUSDT",'01/09/2022')

# 1.4 Write a function (in Python, R or Julia) that retrieves 75 observations of klines data for a generic currency pair since a generic date. The function should take the currency pair and start date as input parameters.
print(retrieves_data("BTCUSDT",'01/09/2022'))
# Please see above.

# 2 The rest is about the FRED API:
# 2.1 Read how authentication with API keys works. Create an account and obtain your own key.
# Account: crawfish***@gmail.com
# Own key: afaa25582e5b8*****cd17b6f1070fa

# 2.2 What is the root URL?
# https://api.stlouisfed.org/

# 2.3 What is the endpoint to retrieve time series observations?
# "/fred/series/observations"

# 2.4 Construct a query string to retrieve the series of the monthly unemployment rate (seasonally adjusted) since 2020-01. Use the fake API key in the query string.abc123
# https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&frequency=m&realtime_start=2020-01-01&api_key=abc123
