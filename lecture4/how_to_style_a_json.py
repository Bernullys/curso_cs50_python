import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(json.dumps(response.json(), indent=2))