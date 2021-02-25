import requests

# URL
url = "https://reqres.in/api/users/2"
response = requests.delete(url)
print(response.status_code)
print(response.is_redirect)

assert response.status_code == 204