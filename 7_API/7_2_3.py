import requests

payload = {'q': 'python'}
response = requests.get('https://www.google.ru/', params=payload)
print(response.url)