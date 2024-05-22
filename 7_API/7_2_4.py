import requests

payload = {'userId': '3', 'id': '29'}
r = requests.get('https://jsonplaceholder.typicode.com/posts', params=payload)
print(r.url)
print(r.content)