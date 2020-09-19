import requests
from bs4 import BeautifulSoup

currencyFrom = "eur"
currencyTo = "uah"
amount = "100"

url = "https://exchangerate.guru/" + currencyFrom+"/"+ currencyTo +"/" +amount + "/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
table = soup.find_all('table', class_="table table-condensed table-bordered")
value = soup.find_all('strong', class_="pretty-sum")

print(amount + " " + currencyFrom +" to " + currencyTo + " = " +value[2].text)