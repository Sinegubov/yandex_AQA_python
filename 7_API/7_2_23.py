import requests

updated_product = {
    "title": "dell",
    "price": "1500"
}

response = requests.patch("https://dummyjson.com/products/10", data=updated_product)
print( response.status_code)
print( response.json())