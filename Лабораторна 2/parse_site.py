import requests
from bs4 import BeautifulSoup

currencyFrom = "eur"
currencyTo = "uah"
amount = "100"

url = "https://exchangerate.guru/" + currencyFrom+"/"+ currencyTo +"/" +amount + "/"

page = requests.get(url) # Get page

soup = BeautifulSoup(page.content, "html.parser") # Init beautiful soup
value = soup.find_all('strong', class_="pretty-sum") # Get html tag with class pretty-sum

print(amount + " " + currencyFrom +" to " + currencyTo + " = " +value[2].text) # Print value