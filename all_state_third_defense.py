import requests
import re
from bs4 import BeautifulSoup
from csv import writer

response = requests.get(
    'https://www.dallasnews.com/high-school-sports/football/2021/02/26/the-2020-21-texas-sports-writers-association-class-6a-all-state-high-school-football-team/')

soup = BeautifulSoup(response.text, 'html.parser')

players = soup.find(class_='body-text')


with open('Texas high school Third team Defense.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['D-line', 'LB 1', 'LB 2', 'LB 3', 'LB 4',
               'DB 1', 'DB 2', 'DB 3', 'Punter', 'Kick returner']
    csv_writer.writerow(headers)

    for player in players:
        linemen = list(player.stripped_strings)[173]
        #print(linemen)
        lb_1 = list(player.stripped_strings)[175]
        #print(lb_1)
        lb_2 = list(player.stripped_strings)[176]
        #print(lb_2)
        lb_3 = list(player.stripped_strings)[177]
        #print(lb_3)
        lb_4 = list(player.stripped_strings)[178]
        #print(lb_4)
        db_1 = list(player.stripped_strings)[181]
        #print(db_1)
        db_2 = list(player.stripped_strings)[183]
        #print(db_2)
        db_3 = list(player.stripped_strings)[185]
        #print(db_3)
        punter = list(player.stripped_strings)[188]
        #print(punter)
        kr = list(player.stripped_strings)[190]
        print(kr)
        csv_writer.writerow([linemen, lb_1, lb_2, lb_3, lb_4, db_1, db_2, db_3, punter, kr])