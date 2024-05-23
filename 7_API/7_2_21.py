import requests

updated_profile = {"name": "Николай Пржевальский", "about": "Первопроходец"}
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjI2NDBjYmYwYTExODAwM2QyZDBmNzMiLCJpYXQiOjE3MTYzOTIzOTQsImV4cCI6MTcxNjk5NzE5NH0.FzocCGDLRSfgZ6JsgMKgYg-56aDYyQKU9i1hh1ANP6o'
response = requests.patch("https://qa-mesto.praktikum-services.ru/api/users/me",
                          headers={'Authorization': token},
                          data=updated_profile)
print(response.status_code)
print(response.json())