import urllib.parse
import requests

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

#validate for py2 as urlib is py3
address = 'lhr'
url = main_api + urllib.parse.urlencode({'address' : address})

json_data = requests.get(url).json()
print(json_data)
