'''import requests

headers = {
	'Content-Type':'application/json',
	'Authorization':'Token 523749432a6d9303b53f47840e38883136af1e6f'
	}
	
def get_meta_data(Ticker):
	url = "https://api.tiingo.com/tiingo/daily/{}".format(ticker)
	response = requests.get(url, headers=headers)
	return response.json()
	
	'''
	
import yfinance as yf

import json	
	
import requests

headers = {
        'Content-Type': 'application/json',
        'Authorization' : 'Token 523749432a6d9303b53f47840e38883136af1e6f'
        }
def get_meta_data(ticker):
	response = requests.get("https://api.tiingo.com/tiingo/daily/{}".format(ticker), headers=headers)
	return response.json()

def get_price_data(ticker):

	ticker = yf.Ticker("%s" % ticker)
	data = ticker.history(period = "30d")
				# convert data into standard format
	data = data.drop(columns = ['Dividends' , 'Stock Splits']) 
	result = data.to_json()
	return result



