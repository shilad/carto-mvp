from bs4 import BeautifulSoup
from requests import get

urls = ['https://tools.wmflabs.org/enwp10/cgi-bin/list2.fcgi?run=yes&projecta=Food_and_drink&namespace=&pagename=&quality=&importance=&score=&limit=1000&offset=1&sorta=Quality&sortb=Quality',
             'https://tools.wmflabs.org/enwp10/cgi-bin/list2.fcgi?run=yes&projecta=Food_and_drink&namespace=&pagename=&quality=&importance=&score=&limit=1000&offset=1001&sorta=Quality&sortb=Quality',
             'https://tools.wmflabs.org/enwp10/cgi-bin/list2.fcgi?run=yes&projecta=Food_and_drink&namespace=&pagename=&quality=&importance=&score=&limit=1000&offset=2001&sorta=Quality&sortb=Quality',
             'https://tools.wmflabs.org/enwp10/cgi-bin/list2.fcgi?run=yes&projecta=Food_and_drink&namespace=&pagename=&quality=&importance=&score=&limit=1000&offset=3001&sorta=Quality&sortb=Quality',
             'https://tools.wmflabs.org/enwp10/cgi-bin/list2.fcgi?run=yes&projecta=Food_and_drink&namespace=&pagename=&quality=&importance=&score=&limit=1000&offset=4001&sorta=Quality&sortb=Quality'
             ]

titles = []

for url in urls:
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    center = soup.find('center')
    rows = center.find_all('tr')
    for i in range(1, 1001):
        title = rows[i].find_all('td')
        titles.append(title[1].a.text.strip())

with open('data.csv', 'w') as f:
    for item in titles:
        f.write("%s\n" % item)





