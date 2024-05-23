import requests

def test_updated_profile():
    updated_profile = {"name": "Николай Пржевальский", "about": "Первопроходец"}
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjI2NDBjYmYwYTExODAwM2QyZDBmNzMiLCJpYXQiOjE3MTYzOTIzOTQsImV4cCI6MTcxNjk5NzE5NH0.FzocCGDLRSfgZ6JsgMKgYg-56aDYyQKU9i1hh1ANP6o'
    response = requests.patch("https://qa-mesto.praktikum-services.ru/api/users/me",
                              headers={'Authorization': token}, data=updated_profile)

    assert response.status_code == 200
    assert response.json()['data']['name'] == 'Николай Пржевальский'
    assert response.json()['data']['about'] == 'Первопроходец'
    