import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for times in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup.findAll('a')
    print ("Retrieving: ", url)

    for tag in tags:
        url = tag.get('href')
        url = tags[position - 1].get('href')

print ("Retrieving: ", url)
