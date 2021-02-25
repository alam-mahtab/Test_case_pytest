import requests
import json
import jsonpath
url = "https://reqres.in/api/users/2"

def test_update():
# Read Input Json File
    file = open('C:\\mydata\\new_user.json','r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)


    # Making a PUT request
    response = requests.put(url, request_json)
    print(response.content)
    print(response.status_code)

    # validating response code
    assert response.status_code == 200

    # fetch header from response
    print(response.headers)
    print("hello")
    print(response.headers.get('Content-length'))

    # parse response to JSON Format
    response_json = json.loads(response.text)

    # Pick id using JSON Path
    updatedAt = jsonpath.jsonpath(response_json,'updatedAt')
    print(updatedAt[0])