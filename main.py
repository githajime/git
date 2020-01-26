print("hello world")

import json
import requests 

url = 'https://disclosure.edinet-fsa.go.jp/api/v1/documents.json'

params = {
    "date" : "2019-04-15",
    "type" : 2
    }

r = requests.get(url, params=params, verify=False)
result = json.loads(r.text)

print(result["metadata"])
