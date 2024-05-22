import requests

response = requests.delete("https://fakestoreapi.com/products/6")
print(response.status_code)
print(response.json())