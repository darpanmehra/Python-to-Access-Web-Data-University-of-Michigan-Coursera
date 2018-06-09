import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET

url = input ('Enter Location - ')
html = urllib.request.urlopen(url).read()
xml = ET.fromstring(html)

comment_counts = xml.findall('.//count')

sum = 0
for count in comment_counts:
    sum = sum + int(count.text)

print ('Sum = ' + str(sum))
