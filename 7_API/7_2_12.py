import json
import requests

payload = {
    "item": "pear",
    "price": "5$"
}
payload_string = json.dumps(payload)
print(payload_string)
r = requests.post('https://httpbin.org/post', data=payload_string)
print(r.json())