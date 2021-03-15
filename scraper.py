import requests 
import re
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://www.texasfootball.com/recruiting/rankings/?ref=subnav')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find(class_='c-rcrt-rankings__list')
print(posts)
with open('recruits(class of 2021).csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Name', 'Rank', 'Commited', 'Position', 'Position rank', 'School']
    csv_writer.writerow(headers)

    for item in posts:
        names = item.find('span').get_text()
        ranks = item.find(class_='c-rcrt-rankings__list-player-col c-rcrt-rankings__list-player-col-rank').get_text()
        position = list(item.stripped_strings)[4]
        position_rank = list(item.stripped_strings)[5]
        school = list(item.stripped_strings)[2]
        commited = item.find(class_='c-rcrt-rankings__list-player-commit-mbl').get_text()
        #print(list(item.stripped_strings))
        csv_writer.writerow([names, ranks, commited, position, position_rank, school])
        
   
        
    





 
  


