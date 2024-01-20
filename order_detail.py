import json
import requests




def find_key(data, target_key):
    queue = [data]
    while len(queue) > 0:
        current = queue.pop(0)
        if type(current) == dict:
            for key in current:
                if key == target_key:
                    return {key: current[key]}
                if isinstance(current[key], (list, dict)):
                    queue.append(current[key])
        elif type(current) == list:
            queue.extend(current)
    return None

def order_detail(orderid, appUin, custom_cookie=None):
    url = "https://channels.weixin.qq.com/shop-faas/mmchannelstradeorder/api/getOrder"
    params = {
        "orderid": orderid,
        "appUin": appUin,
    }
    headers = {
        "Host": "channels.weixin.qq.com",
        "Connection": "keep-alive",
        "xweb_xhr": "1",
        "Cookie": custom_cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090819)XWEB/8519",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Accept-Language": "*",
        "Accept-Encoding": "gzip, deflate, br"
    }

    response = requests.get(url, params=params, headers=headers)

    json_data = json.loads(response.text)
    code = json_data["code"]
    if code != 0:
        return ""

    addressInfo = find_key(json_data, "addressInfo")["addressInfo"]
    print(addressInfo)
    userName = addressInfo["userName"]
    postalCode = addressInfo["postalCode"]
    provinceName = addressInfo["provinceName"]
    cityName = addressInfo["cityName"]
    countyName = addressInfo["countyName"]
    detailInfo = addressInfo["detailInfo"]
    nationalCode = addressInfo["nationalCode"]
    telNumber = addressInfo["telNumber"]

    total_address = provinceName + cityName + countyName + detailInfo
    return userName,telNumber,total_address
