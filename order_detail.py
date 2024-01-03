import requests
import json
import pickle
import agent
from threading import Thread
import time
import requests
from io import BytesIO
import os
from PIL import Image
import qrcode

requests.packages.urllib3.disable_warnings()
from save_class import Order



def order_detail(orderid, appUin, custom_cookie=None):
    url = "http://localhost:8569/getdetail"
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
