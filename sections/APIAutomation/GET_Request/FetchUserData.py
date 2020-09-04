import requests

# API URL
url = "https://reqres.in/api/users?page=2"

# Send Get Request
response = requests.get(url)
print(response)

# Validate Status Code
assert response.status_code == 200
# Fetch Response Header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))

# Fetch Cookies
print(response.cookies)
# Fetch Encoding
print(response.encoding)

print(response.elapsed)
