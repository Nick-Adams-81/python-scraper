import requests 
import re
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://www.texasfootball.com/recruiting/rankings/?ref=subnav')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find(class_='c-rcrt-rankings__list')


with open('recruits.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['name', 'rank', 'commited']
    csv_writer.writerow(headers)

    for item in posts:
        names = item.find('span').get_text()
        #print(names)
        ranks = item.find(class_='c-rcrt-rankings__list-player-col c-rcrt-rankings__list-player-col-rank').get_text()
        #print(ranks)
        position = item.find(class_='c-rcrt-rankings__list-player-col').get_text()
        print(position)
        commited = item.find(class_='c-rcrt-rankings__list-player-commit-mbl').get_text()
        #print(commited)




        csv_writer.writerow([names, ranks, commited])
        
   
        
    





 
  


