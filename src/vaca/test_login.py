import requests

requests.packages.urllib3.disable_warnings()
import requests
import json


def test_login(custom_cookie):
    url = "https://channels.weixin.qq.com/shop-faas/mmchannelstradeorder/api/getList"
    headers = {
        "Host": "channels.weixin.qq.com",
        "Connection": "keep-alive",
        "xweb_xhr": "1",
        "Cookie": custom_cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8519",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Accept-Language": "*",
    }
    params = {
        "orderStatus": "-1",
        "pageNum": "1",
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    root = json.loads(response.text)
    code = root["code"]
    return code == 0
