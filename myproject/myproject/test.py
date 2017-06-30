""" 
import requests
from bs4 import BeautifulSoup

url = 'https://www.dropbox.com/sh/ttquig1dmjfz5uy/AABuwpGz6EQO0NEai3x9eoOYa?dl=0'

def get_all():
    soup = BeautifulSoup(requests.get(url).text)
    for a in soup.find('div',{'class': 'catlist'}).find_all('a'):
        yield 'teste'+a['href']
    print(soup)

get_all() """


import requests
from bs4 import BeautifulSoup

games_url = 'https://www.dropbox.com/sh/ttquig1dmjfz5uy/AABuwpGz6EQO0NEai3x9eoOYa?dl=0'

def get_all_games():
    soup = BeautifulSoup(requests.get(games_url).text)

    for a in soup.find('div', {'class': 'catlist'}).find_all('a'):
        print('http://www.primarygames.com' + a['href'])

get_all_games()