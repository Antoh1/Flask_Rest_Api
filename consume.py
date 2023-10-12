import requests

url = 'http://127.0.0.1:5000/'

response = requests.put(url + '/user/4', {'likes': 20})

print(response.json())