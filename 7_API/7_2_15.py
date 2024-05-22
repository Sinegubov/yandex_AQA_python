import json
import requests

def test_title_json():
    payload = {
        "title": 'Data Serialization',
        "userId": "5"
    }

    headers = {"Content-type": "application/json"}
    payload_string = json.dumps(payload)
    r = requests.post('https://dummyjson.com/posts/add', data=payload_string, headers=headers)

    assert r.json()["title"] == "Data Serialization"
    assert r.json()["userId"] == "5"