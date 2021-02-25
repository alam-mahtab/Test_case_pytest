import requests
import json
import jsonpath
url = "https://reqres.in/api/users?page=2"
def test_get():

    response = requests.get(url)
    print(response)

    #Response content
    print(response.content)

    #Response Header
    print(response.headers)
    print("hello")
    #Parse response to JSON Format
    json_response = json.loads(response.text)
    print(json_response)

    # Fetch value Using json_path
    pages = jsonpath.jsonpath(json_response,'total_pages')
    print(pages[0])
    assert pages[0] == 2

