import datetime

import requests

requests.packages.urllib3.disable_warnings()
import requests
import json

from save_class import Order


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


def get_order_list(page_num, nextKey=None, custom_cookie=None):
    result = []
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
        "Accept-Encoding": "gzip, deflate, b"
    }
    params = {
        "orderStatus": "-1",
        "pageNum": page_num,
        "nextKey": nextKey,
    }
    response = requests.get(url, headers=headers, params=params)
    root = json.loads(response.text)
    code = root["code"]
    if code != 0:
        return result
    try:
        bizuin = find_key(root, "bizuin")["bizuin"]
    except:
        bizuin = ""
    nextKey = root["nextKey"]
    totalPage = root["totalPage"]
    totalNum = root["totalNum"]
    orders = root["orders"]
    for order in orders:
        orderId = order["orderId"]
        createTime = order["createTime"]
        createTime = datetime.datetime.fromtimestamp(createTime)
        status = order["status"]
        if status == 250:
            status = "已取消"
        elif status == 100:
            status = "已完成"
        elif status == 20:
            status = "待发货"
        elif status == 30:
            status = "已发货"
        addressInfo = order["addressInfo"]
        userName = addressInfo["userName"]
        postalCode = addressInfo["postalCode"]
        provinceName = addressInfo["provinceName"]
        cityName = addressInfo["cityName"]
        countyName = addressInfo["countyName"]
        detailInfo = addressInfo["detailInfo"]
        nationalCode = addressInfo["nationalCode"]
        telNumber = addressInfo["telNumber"]
        total_address = provinceName + cityName + countyName + detailInfo
        list_product = order["list"]
        for product in list_product:
            goodsName = product["title"]
            productCnt = product["productCnt"]
            temp = Order(orderId, createTime, status, goodsName, productCnt, userName, telNumber, total_address,
                         nextKey, bizuin, totalPage,
                         totalNum)
            result.append(temp)

    return result
