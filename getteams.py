import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.fifa.com/worldcup/teams/index.html').content

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all(class_='team-name'):
    print(tag.text)

with open('team-names-master.txt', 'w') as f:
    for tag in soup.find_all(class_='team-name'):
        f.write(tag.text+'\n')