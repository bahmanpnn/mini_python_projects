import requests
import json
import cryptocompare


data=cryptocompare.get_price('eth',currency='usd',full=True)
print(data["RAW"]["ETH"]["USD"]["PRICE"])
print(data["RAW"]["ETH"]["USD"]['HIGHDAY'])
print(data["RAW"]["ETH"]["USD"]['LOWDAY'])
# print(data)


# url='https://data-api.cryptocompare.com/asset/v1/data/by/symbol?asset_symbol=BTC'
url = 'https://min-api.cryptocompare.com/data/price?fsym={currency}&tsyms=USD'

# api=requests.get(url).text
# print(api)

print('------------------------')
def get_price_usd(currency):
    resp = requests.get(url.format(currency=currency)).json()
    print('price: ',resp['USD'])


get_price_usd('bnb')
