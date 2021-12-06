import requests
import json

url = "https://reqres.in/api/users​"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

#1
users_data = json.loads(response.text)["data"]

print(users_data)

#2
print("")
payload = json.dumps({
  "name": "Ignacio",
  "job": "Profesor"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

created_user = response.text
print(created_user)

#3
url = "https://reqres.in/api/users​/2"

payload = json.dumps({
  "name": "Morpheus",
  "residence": "zion"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)
updated_user = response.text
print("")
print(updated_user)

#4

url = "https://reqres.in/api/users​/2"

payload = json.dumps({})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
print(response)