import requests 
import re
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://www.texasfootball.com/recruiting/rankings/?ref=subnav')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find(class_='c-rcrt-rankings__list')
#print(posts.span.text)


with open('recruits.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['name', 'rank']
    csv_writer.writerow(headers)

    for item in posts:
        names = soup.find_all('span')
        for name in names:
            print(name.text)
            csv_writer.writerow([name.text])
        ranks = soup.find_all(class_='c-rcrt-rankings__list-player-col c-rcrt-rankings__list-player-col-rank')
        for rank in ranks:
            print(rank.text)
            csv_writer.writerow([rank.text])
        #print(name)
        
        
    





 
  


