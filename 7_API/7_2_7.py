import requests

response = requests.post("https://qa-mesto.praktikum-services.ru/api/cards", data={
    "name": "Красивое место",
    "link": "https://code.s3.yandex.net/qa-automation-engineer/python/files/photoSelenide.jpeg"
}, headers={'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjI2NDBjYmYwYTExODAwM2QyZDBmNzMiLCJpYXQiOjE3MTYzOTIzOTQsImV4cCI6MTcxNjk5NzE5NH0.FzocCGDLRSfgZ6JsgMKgYg-56aDYyQKU9i1hh1ANP6o'})


print(response.status_code)
