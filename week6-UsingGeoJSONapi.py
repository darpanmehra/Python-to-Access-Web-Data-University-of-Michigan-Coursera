import json
import urllib.request, urllib.parse, urllib.error

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})

    print ('Retrieving ',url)
    url_handle = urllib.request.urlopen(url)
    data = url_handle.read()

    print ('Retrieved',len(data),'characters')
    json_data = json.loads(data)

    print ('Place id',json_data['results'][0]['place_id'])
