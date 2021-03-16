from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/chromedriver')
driver.get('https://247sports.com/Season/2021-Football/CompositeRecruitRankings/?InstitutionGroup=highschool&State=TX')

search = driver.find_element_by_class_name('rankings-page__list')
print(search.text)




#with open('Texas high school recruits(class of 2021).csv', 'w') as csv_file:
    #csv_writer = writer(csv_file)
    #headers = ['Name', 'Rank', 'School', 'Position', 'Position rank', 'Commited']
    #csv_writer.writerow(headers)
  






