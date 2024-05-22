import requests


def test_status_code():
    response = requests.get('http://catfact.ninja/fact')
    print(response.status_code)
    print(response.text)
    assert 200 == response.status_code
