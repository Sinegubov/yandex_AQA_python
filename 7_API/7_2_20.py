import requests

updated_product = {
    "title": 'test product',
    "price": 13.5,
    "category": 'electronic'
}

response = requests.patch("https://fakestoreapi.com/products/7", data=updated_product)
print(response.status_code)
print(response.text)