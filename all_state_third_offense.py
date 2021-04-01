import requests
import re
from bs4 import BeautifulSoup
from csv import writer

response = requests.get(
    'https://www.dallasnews.com/high-school-sports/football/2021/02/26/the-2020-21-texas-sports-writers-association-class-6a-all-state-high-school-football-team/')

soup = BeautifulSoup(response.text, 'html.parser')

players = soup.find(class_='body-text')


with open('Texas high school Third team Offense.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['QB', 'RB-1', 'RB-2', 'RB-3', 'FB', 'Guard-1', 'Guard-2', 'Tackle-1',
               'Tackle-2', 'Center', 'WR-1', 'WR-2', 'TE-1', 'TE-2', 'All-Purpose', 'PK']
    csv_writer.writerow(headers)

    for player in players:
        qb = list(player.stripped_strings)[159]
        #print(qb)
        rb_1 = list(player.stripped_strings)[162]
        #print(rb_1)
        rb_2 = list(player.stripped_strings)[163]
        #print(rb_2)
        rb_3 = list(player.stripped_strings)[164]
        #print(rb_3)
        fullback = list(player.stripped_strings)[166]
        #print(fullback)
        guards_1 = list(player.stripped_strings)[139]
        #print(guards_1)
        guards_2 = list(player.stripped_strings)[140]
        #print(guards_2)
        tackle_1 = list(player.stripped_strings)[142]
        #print(tackle_1)
        tackle_2 = list(player.stripped_strings)[143]
        #print(tackle_2)
        center = list(player.stripped_strings)[146]
        #print(center)
        receiver_1 = list(player.stripped_strings)[149]
        #print(receiver_1)
        receiver_2 = list(player.stripped_strings)[151]
        #print(receiver_2)
        tight_end_1 = list(player.stripped_strings)[154]
        #print(tight_end_1)
        tight_end_2 = list(player.stripped_strings)[156]
        #print(tight_end_2)
        ap = list(player.stripped_strings)[168]
        #print(ap)
        pk = list(player.stripped_strings)[170]
        #print(pk)
        csv_writer.writerow([qb, rb_1, rb_2, rb_3, fullback, guards_1, guards_2, tackle_1, tackle_2, center, receiver_1, receiver_2,
                             tight_end_1, tight_end_2, ap, pk])

