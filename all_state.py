from selenium import webdriver
from csv import writer
import pandas as pd
import time

driver = webdriver.Chrome('/chromedriver')
url = 'https://www.dallasnews.com/high-school-sports/football/2021/02/26/the-2020-21-texas-sports-writers-association-class-6a-all-state-high-school-football-team/'
driver.get(url)
