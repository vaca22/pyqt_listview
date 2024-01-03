import requests
import json

def query_cookie():
    url = "http://localhost:8569/getcookie"
    response = requests.post(url)
    json_data = json.loads(response.text)
    json_data = json_data["data"]
    cookie= json_data["cookie"]
    return cookie