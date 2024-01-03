import requests
import json

from query_cookies import query_cookie


def query_login(ticket):
    url = "http://localhost:8569/getstatus"
    response = requests.post(url)
    json_data = json.loads(response.text)
    json_data = json_data["data"]
    status = json_data["status"]
    print(status)

    if status == 3:
        cookies = query_cookie()
        with open('cookies.txt', 'w') as f:
            f.write(cookies)

    return status