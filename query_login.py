import requests
import json




def query_login(ticket):
    url = "https://channels.weixin.qq.com/shop-faas/mmecnodelogin/queryLoginQrCode"
    params = {
        "token": "",
        "lang": "zh_CN",
        "qr_ticket": ticket,
        "isWxWork": "0"
    }
    headers = {
        "Host": "channels.weixin.qq.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://channels.weixin.qq.com/shop",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ja-JP;q=0.6,ja;q=0.5"
    }

    response = requests.get(url, params=params, headers=headers)

    json_data = json.loads(response.text)

    status = json_data["status"]
    print(status)

    if status == 3:
        cookies = response.cookies
        cookies_dict = cookies.get_dict()
        print(cookies_dict)
        with open('cookies.txt', 'w') as f:
            f.write(str(cookies_dict))

    return status