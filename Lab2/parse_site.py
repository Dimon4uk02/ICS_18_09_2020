import requests
from bs4 import BeautifulSoup

currencyFrom = "eur" # Валюта, яку ми продаємо
currencyTo = "uah" # Валюта, яку ми купляємо
amount = "100" # Кількість валюти

url = "https://exchangerate.guru/" + currencyFrom + "/"+ currencyTo +"/" +amount + "/" # Посилання

page = requests.get(url) # Скачуємо код сторінки

soup = BeautifulSoup(page.content, "html.parser") # Ініціалізуємо BeautifulSoup

value = soup.find_all('strong', class_="pretty-sum") # Отримуємо елементи тегу 'strong' з класом 'pretty-sum'

result = value[2].text # Проаналізувавши сторіку, завжди 3 елемент буде з потрібним мені значенням

print(amount + " " + currencyFrom +" to " + currencyTo + " = " + result) # Виводимо значення