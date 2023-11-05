#!/usr/bin/python3
import requests

# Define the URL for the CoinGecko API to get the BTC to USD exchange rate
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=ars"

# Send an HTTP GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()

    # Check if 'bitcoin' is in the response
    if 'bitcoin' in data:
        btc_data = data['bitcoin']

        # Check if 'usd' is in the bitcoin data
        if 'ars' in btc_data:
            btc_to_ars = btc_data['ars']
            print(f"Current Bitcoin (BTC) rate in ars: {btc_to_ars} ars")
        else:
            print("ars rate not found in API response")
    else:
        print("Bitcoin data not found in API response")
else:
    print("Failed to retrieve data")