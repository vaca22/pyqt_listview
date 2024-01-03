import datetime

import requests
import json
import openpyxl

import os

workbook = openpyxl.Workbook()
worksheet = workbook.active

def init_xml(path):
    global workbook
    global worksheet

    if os.path.exists(path):
        os.remove(path)
    worksheet.append(["订单号", "时间", "状态", "商品名称", "数量", "收货地址"])


def append_xml(orderId, createTime, status, goodsName, productCnt, total_address):
    global worksheet
    worksheet.append([orderId, createTime, status, goodsName, productCnt, total_address])


def save_xml(path):
    global workbook
    workbook.save(path)
