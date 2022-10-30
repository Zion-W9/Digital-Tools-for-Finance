import requests

# 1 The first part is about the Binance API:
# 1.1 What is the root URL?
print("https://api.binance.com")

# 1.2 What is the endpoint to retrieve klines (open-high-low-close data) for a specific cryptocurrency?
print('/api/v3/klines')

# 1.3 Specify a request string to retrieve 75 observations of klines data for BTCUSDT since 2022-09-01.
def retrieves_data()