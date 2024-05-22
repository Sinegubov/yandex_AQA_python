import requests

payload = {"email": "sinegubov_8@gmail.com", 'password': "123"}
response = requests.post("https://qa-mesto.praktikum-services.ru/api/signup", data=payload)

print(response.status_code)
print(response.text)

# напиши здесь свой код