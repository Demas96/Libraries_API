import requests


url = 'https://opendata.mkrf.ru/v2/libraries/$'
headers = {'content-type': 'application/json', 'X-API-KEY': 'ba73521d9c5049baed810349f63239baf6f4562244229965a408a5b9021b6a33'}
r = requests.get(url, headers=headers)
data = r.json()['data']
for i in data:
    print(i['data']['general']['contacts'])