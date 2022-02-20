import requests
from bs4 import BeautifulSoup

url = 'https://vk.com/album290464528_000'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)


def testtt():
    pass