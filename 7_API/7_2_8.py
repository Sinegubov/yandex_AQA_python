import requests

payload = {'user': 'root', 'password': 'qwerty'}
response = requests.post('https://httpbin.org/post', data=payload)

print(response.json()['form'])
# {'password': 'qwerty', 'user': 'root'}