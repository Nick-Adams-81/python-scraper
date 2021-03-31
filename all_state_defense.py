import requests
import re
from bs4 import BeautifulSoup
from csv import writer

response = requests.get(
    'https://www.dallasnews.com/high-school-sports/football/2021/02/26/the-2020-21-texas-sports-writers-association-class-6a-all-state-high-school-football-team/')

soup = BeautifulSoup(response.text, 'html.parser')

players = soup.find(class_='body-text')

with open('Texas high school First team Defense.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['D-line 1', 'D-line 2', 'D-line 3', ' D-line 4', 'LB 1', 'LB 2', 'LB 3', 'LB 4',
               'DB', 'Punter', 'Kick returner', 'D Player of the year', 'Coach of the year']
    csv_writer.writerow(headers)

    for player in players:
        linemen_1 = list(player.stripped_strings)[58]
        print(linemen_1)
        linemen_2 = list(player.stripped_strings)[60]
        print(linemen_2)
        linemen_3 = list(player.stripped_strings)[62]
        print(linemen_3)
        linemen_4 = list(player.stripped_strings)[63]
        print(linemen_4)
        lb_1 = list(player.stripped_strings)[66]
        print(lb_1)
        lb_2 = list(player.stripped_strings)[67]
        print(lb_2)
        lb_3 = list(player.stripped_strings)[68]
        print(lb_3)
        lb_4 = list(player.stripped_strings)[69]
        print(lb_4)
        db = list(player.stripped_strings)[71]
        print(db)
        punter = list(player.stripped_strings)[73]
        print(punter)
        kr = list(player.stripped_strings)[76]
        print(kr)
        dpoy = list(player.stripped_strings)[79]
        print(dpoy)
        coach = list(player.stripped_strings)[81]
        print(coach)
        csv_writer.writerow([linemen_1, linemen_2, linemen_3, linemen_4, lb_1, lb_2, lb_3, lb_4, db, punter, kr,
                             dpoy, coach])