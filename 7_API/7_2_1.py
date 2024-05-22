import requests


def test_status_code():
    response = requests.get('https://qa-mesto.praktikum-services.ru/',
                            headers={'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjI2NDBjYmYwYTExODAwM2QyZDBmNzMiLCJpYXQiOjE3MTYzOTIzOTQsImV4cCI6MTcxNjk5NzE5NH0.FzocCGDLRSfgZ6JsgMKgYg-56aDYyQKU9i1hh1ANP6o'})

    print(response.status_code)
    assert 200 == response.status_code
