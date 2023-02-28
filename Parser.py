import requests
from bs4 import BeautifulSoup

# Получаем HTML-страницу
url = 'https://www.example.com'
response = requests.get(url)
html = response.content

# Создаем объект BeautifulSoup и находим нужные элементы
soup = BeautifulSoup(html, 'html.parser')
title = soup.title.string
links = soup.find_all('a')

# Выводим результаты
print('Заголовок страницы:', title)
print('Ссылки на странице:')
for link in links:
    print(link.get('href'))
