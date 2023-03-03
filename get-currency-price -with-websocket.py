import requests
from bs4 import BeautifulSoup


url="https://coinmarketcap.com/currencies/bitcoin/"

response=requests.get(url).content
soup=BeautifulSoup(response,features='html.parser')
price=soup.find('div',attrs={'class':'priceValue'}).text
print(price)

