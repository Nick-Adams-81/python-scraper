import requests
import re
from bs4 import BeautifulSoup
from csv import writer

response = requests.get(
    'https://www.dallasnews.com/high-school-sports/football/2021/02/26/the-2020-21-texas-sports-writers-association-class-6a-all-state-high-school-football-team/')

soup = BeautifulSoup(response.text, 'html.parser')

players = soup.find(class_='body-text')


with open('Texas high school First team Offense.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['QB', 'RB-1', 'RB-2', 'RB-3', 'FB', 'Guards', 'Tackle-1',
               'Tackle-2', 'Center', 'WR-1', 'WR-2', 'TE', 'All-Purpose', 'PK', 'POY']
    csv_writer.writerow(headers)

    for player in players:
        qb = list(player.stripped_strings)[40]
        rb_1 = list(player.stripped_strings)[43]
        rb_2 = list(player.stripped_strings)[44]
        rb_3 = list(player.stripped_strings)[45]
        fullback = list(player.stripped_strings)[47]
        guards = list(player.stripped_strings)[26]
        tackle_1 = list(player.stripped_strings)[29]
        tackle_2 = list(player.stripped_strings)[30]
        center = list(player.stripped_strings)[32]
        receiver_1 = list(player.stripped_strings)[35]
        receiver_2 = list(player.stripped_strings)[36]
        tight_end = list(player.stripped_strings)[38]
        ap = list(player.stripped_strings)[49]
        pk = list(player.stripped_strings)[52]
        poy = list(player.stripped_strings)[54]
        csv_writer.writerow([qb, rb_1, rb_2, rb_3, fullback, guards, tackle_1, tackle_2, center, receiver_1, receiver_2,
                             tight_end, ap, pk, poy])


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
