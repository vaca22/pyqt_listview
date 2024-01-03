import json
import requests

requests.packages.urllib3.disable_warnings()




def order_detail(orderid, appUin, custom_cookie=None):
    url = "http://vaca.vip:8569/getdetail"
    body = {
        "orderid": orderid,
        "appUin": appUin,
        "cookie": custom_cookie
    }
    response = requests.post(url, json=body, verify=False)
    print(response.text)
    json_data = json.loads(response.text)

    json_data = json_data["data"]
    total_address =json_data["detail"]
    return total_address
