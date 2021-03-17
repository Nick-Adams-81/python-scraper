from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('/chromedriver')
driver.get('')

players = driver.find_elements_by_class_name('rankings-page__list-item')

player_list = []

for player in players:
    rank = player.find_element_by_class_name('primary').text
    name = player.find_element_by_class_name('rankings-page__name-link').text
    position = player.find_element_by_class_name('position').text
    metrics = player.find_element_by_class_name('metrics').text
    school = player.find_element_by_class_name('meta').text
    player_info = {
        'rank': rank,
        'name': name,
        'position': position,
        'height / weight': metrics,
        'school': school
    }

    player_list.append(player_info)
    print(player_list)
   
   
#df = pd.DataFrame(player_list)
#print(df)


  

    






  






