import requests 
import re
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://www.texasfootball.com/recruiting/rankings/?ref=subnav')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find(class_='c-rcrt-rankings__list')
#print(posts)


with open('recruits.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['name', 'rank']
    csv_writer.writerow(headers)

    for item in posts:
        names = soup.find_all('span')
        for name in names:
            new_name = name.get_text()
            print(new_name)
            csv_writer.writerow([new_name])
        ranks = soup.find_all(class_='c-rcrt-rankings__list-player-col c-rcrt-rankings__list-player-col-rank')
        for rank in ranks:
            new_rank = rank.get_text()
            print(new_rank)
            csv_writer.writerow([new_rank])
            
   
        
    





 
  


