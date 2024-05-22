import requests

def test_city_name():
    response = requests.get('https://qa-mesto.praktikum-services.ru/api/users/me',
                            headers={'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjI2NDBjYmYwYTExODAwM2QyZDBmNzMiLCJpYXQiOjE3MTYzOTIzOTQsImV4cCI6MTcxNjk5NzE5NH0.FzocCGDLRSfgZ6JsgMKgYg-56aDYyQKU9i1hh1ANP6o'})

    r = response.json()
    print(r)
    assert "sinegubov_8@gmail.com" == r['data']['email']
