import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find_all('span', class_='titleline')


with open('data.txt', 'w') as f:
    for item in data:
        f.write(item.find('a').text) + f.write('   ')
        f.write(item.find('a').get('href')) + f.write('\n')