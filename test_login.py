import requests
requests.packages.urllib3.disable_warnings()
import requests
import json





def test_login(custom_cookie=None):
    page_num = 1
    nextKey = None
    url = "http://vaca.vip:8569/testlogin"
    body = {"cookie": custom_cookie, "pageNum": page_num, "nextKey": nextKey}
    response = requests.post(url, json=body, verify=False)
    print(response.text)
    root = json.loads(response.text)
    print(root)
    root = root["data"]
    code = root["success"]
    return code