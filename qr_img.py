import base64
import time

import requests
import json

from query_login import query_login


def qr_img():
    url = "http://localhost:8569/getqr"


    response = requests.post(url)
    json_data = json.loads(response.text)
    json_data = json_data["data"]
    qrcodeImg = json_data["qrcodeImg"]
    qrTicket = json_data["qrTicket"]

    print(qrcodeImg)
    print(qrTicket)
    base64_string = qrcodeImg
    decoded_bytes = base64.b64decode(base64_string)
    with open('qrcode.png', 'wb') as f:
        f.write(decoded_bytes)

    while True:
        if query_login(qrTicket) == 3:
            break
        time.sleep(2)
