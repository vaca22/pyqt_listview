import requests
requests.packages.urllib3.disable_warnings()
import requests
import json

from save_class import Order


def get_order_list(page_num, nextKey=None, custom_cookie=None):
    result = []
    url = "http://vaca.vip:8569/getlist"

    body = {
        "pageNum": page_num,
        "nextKey": nextKey,
        "cookie": custom_cookie
    }
    response = requests.post(url, json=body, verify=False)
    print(response.text)
    root = json.loads(response.text)
    root = root["data"]["orderBeans"]

    for i in range(len(root)):
        orderId = root[i]["orderId"]
        createTime = root[i]["createTime"]
        status = root[i]["status"]
        # status 250 已取消 100 已完成 20 待发货
        if status == 250:
            status = "已取消"
        elif status == 100:
            status = "已完成"
        elif status == 20:
            status = "待发货"

        goodsName = root[i]["goodsName"]
        productCnt = root[i]["productCnt"]
        total_address = root[i]["total_address"]
        nextKey = root[i]["nextKey"]
        bizuin = root[i]["bizuin"]
        totalPage = root[i]["totalPage"]
        totalNum = root[i]["totalNum"]
        temp = Order(orderId, createTime, status, goodsName, productCnt, total_address, nextKey, bizuin, totalPage,
                     totalNum)
        result.append(temp)
    return result
