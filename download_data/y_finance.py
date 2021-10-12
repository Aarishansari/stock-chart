
import yfinance as yf
import json	
import requests


headers = {
        'Content-Type': 'application/json',
        'Authorization' : 'Token 523749432a6d9303b53f47840e38883136af1e6f'
        }
def get_meta_data(ticker):
	response = requests.get("https://api.tiingo.com/tiingo/daily/{}".format(ticker), headers=headers)
	description = response.json()
	return description




