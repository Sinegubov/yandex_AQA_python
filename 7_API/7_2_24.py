import requests

updated_avatar = {"avatar": "https://pictures.s3.yandex.net/resources/jacques-cousteau_1604393756.png"}
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjI2NDBjYmYwYTExODAwM2QyZDBmNzMiLCJpYXQiOjE3MTYzOTIzOTQsImV4cCI6MTcxNjk5NzE5NH0.FzocCGDLRSfgZ6JsgMKgYg-56aDYyQKU9i1hh1ANP6o'
response = requests.patch("https://qa-mesto.praktikum-services.ru/api/users/me/avatar",
                          headers={'Authorization': token},
                          data=updated_avatar)
print(response.status_code)
print(response.json())