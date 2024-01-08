import requests
import json


def get_info_name(custom_cookie):
    return_name = "店铺名："
    url = 'https://channels.weixin.qq.com/shop-faas/mmchannelstradehome/api/home'
    headers = {
        'Connection': 'keep-alive',
        'xweb_xhr': '1',
        "Cookie": custom_cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819) XWEB/8531',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_data = json.loads(response.text)
        baseInfo = json_data["baseInfo"]
        iconUrl = baseInfo["iconUrl"]
        nickName = baseInfo["nickName"]
        return_name += nickName
    else:
        pass
    return return_name
