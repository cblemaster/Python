# Note you need to run 'pip install requests' to use the requests module
import requests

people = requests.get('http://api.open-notify.org/astros.json')
json  = people.json()

print(json)

print('The people currently in space are:')
for person in json['people']:
    print(person['name'])
