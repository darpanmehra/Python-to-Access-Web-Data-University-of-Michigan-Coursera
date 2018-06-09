import urllib.request, urllib.parse, urllib.error
import json



url = input('Enter location: ')
print ('Retriving ' + url)
html = urllib.request.urlopen(url).read()
data = json.loads(html)

comment_counts = len(data['comments'])
print(comment_counts)

sum = 0
for num in data['comments']:
    sum = sum + int(num['count'])

print ('Sum: ' + str(sum))
