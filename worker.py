import os


from order_detail import order_detail
from order_list import get_order_list
from qr_img import qr_img
from test_login import test_login
from xml_save import init_xml, append_xml, save_xml

if __name__ == '__main__':
    custom_cookie = None
    # check if 'cookies.txt' exists
    if os.path.exists('cookies.txt'):
        with open('cookies.txt', 'r') as f:
            custom_cookie = f.read()
    print(custom_cookie)
    # print type
    if not test_login(custom_cookie):
        print("登录失败")
        qr_img()
        with open('cookies.txt', 'r') as f:
            custom_cookie = f.read()
    init_xml()
    result_total = []
    result = get_order_list(1, None, custom_cookie)
    result_total.extend(result)
    totalPage = 0
    nextKey = ""
    bizuin = ""
    for order in result:
        if order.bizuin != "":
            bizuin = order.bizuin
        totalPage = order.totalPage
        nextKey = order.nextKey
    print(totalPage)
    for i in range(2, totalPage + 1):
        result = get_order_list(i, nextKey, custom_cookie)
        result_total.extend(result)
        for order in result:
            if order.bizuin != "":
                bizuin = order.bizuin
            nextKey = order.nextKey

    for order in result_total:
        if order.total_address.find("*") != -1:
            order.total_address = order_detail(order.orderId, bizuin, custom_cookie)
        append_xml(order.orderId, order.createTime, order.status, order.goodsName, order.productCnt,
                   order.total_address)
    save_xml()
