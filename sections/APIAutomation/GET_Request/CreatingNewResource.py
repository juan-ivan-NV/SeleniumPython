import requests
import json
import jsonpath

# API URL

url = "https://reqres.in/api/users/2"

file = open('file2.json','r')
json_input = file.read()
request_json = json.loads(json_input)

response = requests.put(url, request_json)

assert response.status_code == 200


response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])