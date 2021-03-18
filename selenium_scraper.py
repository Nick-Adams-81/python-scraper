from selenium import webdriver
from csv import writer
import pandas as pd
import time

driver = webdriver.Chrome('/chromedriver')
driver.get('')


players = driver.find_elements_by_class_name('rankings-page__list-item')
player_list = []
time.sleep(5)

with open('Texas high school recruits(class of 2022).csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Rank', 'Name', 'Position', 'National Position Rank', 'Height / Weight', 'School']
    csv_writer.writerow(headers)

    for player in players:
        rank = player.find_element_by_class_name('primary').text
        name = player.find_element_by_class_name('rankings-page__name-link').text
        position = player.find_element_by_class_name('position').text
        metrics = player.find_element_by_class_name('metrics').text
        school = player.find_element_by_class_name('meta').text
        position_rank = player.find_element_by_class_name('natrank').text
        csv_writer.writerow([rank, name, position, position_rank, metrics, school])
        player_info = {
            'Rank': rank,
            'Name': name,
            'Position': position,
            'Position rank': position_rank,
            'Height / Weight': metrics,
            'School': school
        }
    
        player_list.append(player_info)
    
        players_df = pd.DataFrame(player_list)
        print(players_df)



  

    






  






