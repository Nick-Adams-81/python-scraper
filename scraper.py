import requests 
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find(class_='product_main')


with open('post.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['title', 'price']
    csv_writer.writerow(headers)

    for item in posts:
        title = soup.find('h1').get_text()
        price = soup.find(class_='price_color').get_text()
        csv_writer.writerow([title, price])
    





 
  


