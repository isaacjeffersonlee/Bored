import requests

url = "https://www.boredapi.com/api/activity/"

r = requests.get(url)

print(r.json())
