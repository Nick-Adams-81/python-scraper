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



