import requests
import json  # импортировали библиотеку


def test_add_to_cart_api():
    with open('data.json') as f:  # открыли файл
        data = json.load(f)  # прочитали файл и сохранили данные
        # получили словарь, который можно передать в запросе:
        response = requests.post('http://test.server/add_to_cart', json=data})

        # ...дальше идут проверки