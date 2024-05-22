import json
import requests

payload = {
    "userId": 2,
    "title": "Alea jacta est."
}

payload_string = json.dumps(payload)
headers = {"Content-type": "application/json"}
r = requests.post('https://jsonplaceholder.typicode.com/albums', data=payload_string, headers=headers)

assert r.json()["userId"] == 2
assert r.json()["title"] == "Alea jacta est."
