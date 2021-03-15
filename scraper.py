import requests 
import re
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://www.texasfootball.com/recruiting/rankings/?ref=subnav')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find(class_='c-rcrt-rankings__list')

with open('Texas high school recruits(class of 2022).csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Name', 'Rank', 'School', 'Position', 'Position rank', 'Commited']
    csv_writer.writerow(headers)

    for item in posts:
        names = list(item.stripped_strings)[1]
        ranks = list(item.stripped_strings)[0]
        position = list(item.stripped_strings)[4]
        position_rank = list(item.stripped_strings)[5]
        school = list(item.stripped_strings)[2]
        commited = list(item.stripped_strings)[3]
        csv_writer.writerow([names, ranks, school, position, position_rank, commited])
        
   
        
    





 
  


