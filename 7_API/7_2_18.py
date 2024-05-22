import requests


def test_delete_card():
    url = 'https://qa-mesto.praktikum-services.ru'
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjI2NDBjYmYwYTExODAwM2QyZDBmNzMiLCJpYXQiOjE3MTYzOTIzOTQsImV4cCI6MTcxNjk5NzE5NH0.FzocCGDLRSfgZ6JsgMKgYg-56aDYyQKU9i1hh1ANP6o'

    # добавим новое фото
    response = requests.post(f"{url}/api/cards", data={
        "name": "Замечательное место",
        "link": "https://code.s3.yandex.net/qa-automation-engineer/java/files/paid-track/sprint1/photoSelenide.jpg"
    }, headers={'Authorization': token})

    id_photo = response.json()['data']['_id']

    # удалим фото
    response_delete = requests.delete(f"{url}/api/cards/{id_photo}", headers={'Authorization': token})

    # проверим, что удаление выполнено успешно
    assert response_delete.status_code == 200
