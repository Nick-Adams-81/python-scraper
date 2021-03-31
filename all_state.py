import requests 
import re
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.dallasnews.com/high-school-sports/football/2021/02/26/the-2020-21-texas-sports-writers-association-class-6a-all-state-high-school-football-team/')

soup = BeautifulSoup(response.text, 'html.parser')

players = soup.find(class_='body-text')


for player in players:
    qb = list(player.stripped_strings)[40]
    print(qb)
    rb_1 = list(player.stripped_strings)[43]
    print(rb_1)
    rb_2 = list(player.stripped_strings)[44]
    print(rb_2)
    rb_3 = list(player.stripped_strings)[45]
    print(rb_3)
    fullback = list(player.stripped_strings)[47]
    print(fullback)
    guards = list(player.stripped_strings)[26]
    print(guards)
    tackle_1 = list(player.stripped_strings)[29]
    print(tackle_1)
    tackle_2 = list(player.stripped_strings)[30]
    print(tackle_2)
    center = list(player.stripped_strings)[32]
    print(center)
    receiver_1 = list(player.stripped_strings)[35]
    print(receiver_1)
    receiver_2 = list(player.stripped_strings)[36]
    print(receiver_2)
    tight_end = list(player.stripped_strings)[38]
    print(tight_end)
    ap = list(player.stripped_strings)[49]
    print(ap)
    pk = list(player.stripped_strings)[52]
    print(pk)
    poy = list(player.stripped_strings)[54]
    print(poy)
    




