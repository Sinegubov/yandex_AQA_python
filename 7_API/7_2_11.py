import json
import requests

payload = {
    "name": "Ivan Ivanov",
    "age": "25"
}

payload_string = json.dumps(payload)
r = requests.post('https://httpbin.org/post', data=payload_string)