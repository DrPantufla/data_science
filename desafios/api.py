import json
import requests

def request(requested_url):
    payload={}
    headers = {}

    response = requests.request("GET", requested_url, headers=headers, data=payload)
    return json.loads(response.text)

data = request("https://api.coindesk.com/v1/bpi/historical/close.json")["bpi"]

selected_data = [k for k, v in data.items() if float(v) < 60000]
print(selected_data)