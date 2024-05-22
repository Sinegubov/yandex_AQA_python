import requests

response = requests.get("https://randomuser.me/api/")
r = response.json() # десериализация
print(r)
print(r["results"][0]["gender"])
assert 44 == r["results"][0]["dob"]["age"]
