import requests
import re
from bs4 import BeautifulSoup
from csv import writer

response = requests.get(
    'https://www.dallasnews.com/high-school-sports/football/2021/02/26/the-2020-21-texas-sports-writers-association-class-6a-all-state-high-school-football-team/')

soup = BeautifulSoup(response.text, 'html.parser')

players = soup.find(class_='body-text')


with open('Texas high school Second team Offense.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['QB', 'RB-1', 'RB-2', 'RB-3', 'FB', 'Guards', 'Tackle-1',
               'Tackle-2', 'Center', 'WR-1', 'WR-2', 'TE', 'All-Purpose', 'PK', 'POY']
    csv_writer.writerow(headers)

    for player in players:
        qb = list(player.stripped_strings)[100]
        print(qb)
        rb_1 = list(player.stripped_strings)[102]
        print(rb_1)
        fullback = list(player.stripped_strings)[104]
        print(fullback)
        guards = list(player.stripped_strings)[85]
        print(guards)
        tackle_1 = list(player.stripped_strings)[87]
        print(tackle_1)
        tackle_2 = list(player.stripped_strings)[88]
        print(tackle_2)
        center = list(player.stripped_strings)[90]
        print(center)
        receiver_1 = list(player.stripped_strings)[93]
        print(receiver_1)
        receiver_2 = list(player.stripped_strings)[95]
        print(receiver_2)
        tight_end = list(player.stripped_strings)[98]
        print(tight_end)
        ap = list(player.stripped_strings)[106]
        print(ap)
        pk = list(player.stripped_strings)[109]
        print(pk)
        poy = list(player.stripped_strings)[54]
        csv_writer.writerow([qb, rb_1, fullback, guards, tackle_1, tackle_2, center, receiver_1, receiver_2,
                             tight_end, ap, pk, poy])



