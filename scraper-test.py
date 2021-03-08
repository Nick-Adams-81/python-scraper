from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')


# Direct #
# print(soup.body)
# print(soup.head)
# print(soup.head.title)

# find() #
# el = soup.find('p')
# find_all() or findAll() #
# el = soup.find_all('a')
# el = soup.find_all('p')[1]
# el = soup.find(id='link1')
# el = soup.find(class_='sister')

# get_text() #
# el = soup.find(class_='sister').get_text()

# looping through all items with a sister class

# for item in soup.select('.sister'):
    # print(item.get_text())

# Navigation #
# el = soup.body.contents[1]
# el = soup.find(id='link2').find_previous_sibling()
el = soup.find('p').get_text()


print(el)