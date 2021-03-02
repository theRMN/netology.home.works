from pprint import pprint
import requests
import json

name_list = ['Hulk', 'Captain America', 'Thanos']

intelligence_dict = {}

x = []

for name in name_list:
    url = 'https://superheroapi.com/api/2619421814940190/search/' + name
    resp = requests.get(url)
    intelligence = int(resp.json()['results'][0]['powerstats']['intelligence'])  # We get the IQ
    hero_name = resp.json()['results'][0]['name']  # We get the name of superhero
    intelligence_dict[hero_name] = intelligence
    x.append(intelligence)

for i in intelligence_dict.items():
    if i[1] == max(x):
        print(i[0])

# print(resp.status_code)
# print(resp.content)
# pprint(resp.headers)
# print(resp.text)
# pprint(resp.json())
