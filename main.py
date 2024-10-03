import requests

r = requests.get('https://lolkot.ru/events')
print(r.text)