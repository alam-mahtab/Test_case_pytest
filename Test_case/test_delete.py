import requests

# URL
url = "https://reqres.in/api/users/2"
#url = "http://checkfast.herokuapp.com/users/username?username=string"
def test_delete():
    response = requests.delete(url)
    print(response.status_code)
    print(response.is_redirect)

    assert response.status_code == 204
    #assert response.status_code == 200