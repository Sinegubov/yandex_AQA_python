import requests

url = 'https://qa-mesto.praktikum-services.ru/api/cards'
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjI2NDBjYmYwYTExODAwM2QyZDBmNzMiLCJpYXQiOjE3MTYzOTIzOTQsImV4cCI6MTcxNjk5NzE5NH0.FzocCGDLRSfgZ6JsgMKgYg-56aDYyQKU9i1hh1ANP6o'
response_get = requests.get(f"{url}", headers={'Authorization': token})

card_id = response_get.json()['data'][10]['_id']
print(card_id)
# добавим лайк на фото
response_put = requests.put(f"{url}/{card_id}/likes", headers={'Authorization': token})
# напиши здесь свой код
print(response_put.json()['data']['likes'])

response_del = requests.delete(f"{url}/{card_id}/likes", headers={'Authorization': token})
print(response_del.json()['data']['likes'])
