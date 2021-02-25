import requests
import json
import jsonpath
url = "https://reqres.in/api/users"

def test_create():
    # Read Input Json File
    file = open('C:\\mydata\\new_user.json','r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    # Posting a request
    response = requests.post(url, request_json)
    print(response.content)
    print(response.status_code)
    # validating response code
    assert response.status_code == 201
    # fetch header from response
    print(response.headers)
    print(response.headers.get('Content-length'))
    # parse response to JSON Format
    response_json = json.loads(response.text)
    # Pick id using JSON Path
    id = jsonpath.jsonpath(response_json,'id')
    print(id[0])