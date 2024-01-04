# -*- coding: utf-8 -*-

import base64
import json
import os
import time
from threading import Thread

import requests

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
from cookies_convert import cookie_dict_to_str
from order_detail import order_detail
from order_list import get_order_list
from query_login import query_login
from test_login import test_login
from xml_save import init_xml, append_xml, save_xml


class Ui_Dialog(object):

    def __init__(self):
        self.breakFlag = None
        self.refreshThread = None
        self.custom_cookie = ""
        self.path = "orders.xlsx"
        self.exportThread = None

    def on_pushrefresh_clicked(self):
        print("pushrefresh button was clicked")
        # check if thread is None
        if self.refreshThread is None:
            self.refreshThread = Thread(target=self.readCookies)
            self.refreshThread.start()
            return

        print("thread is alive")

    def on_export_clicked(self):
        if self.exportThread is None:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None, "导出xlsx位置", "",
                                                                "Text Files (*.xlsx)", options=options)
            if fileName:
                fileName = fileName + ".xlsx"
                print(fileName)
                self.path = fileName
                self.exportThread = Thread(target=self.exportData)
                self.exportThread.start()
                return

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(541, 339)
        self.label_qr = QtWidgets.QLabel(Dialog)
        self.label_qr.setGeometry(QtCore.QRect(240, 50, 340, 261))
        self.label_qr.setText("")
        self.label_qr.setObjectName("label_qr")
        self.label_status = QtWidgets.QLabel(Dialog)
        self.label_status.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.label_status.setObjectName("label_status")
        self.pushrefresh = QtWidgets.QPushButton(Dialog)
        self.pushrefresh.setGeometry(QtCore.QRect(10, 40, 91, 24))
        self.pushrefresh.setObjectName("pushrefresh")
        self.pushrefresh.clicked.connect(self.on_pushrefresh_clicked)

        self.exportButton = QtWidgets.QPushButton(Dialog)
        self.exportButton.setGeometry(QtCore.QRect(40, 260, 75, 24))
        self.exportButton.setObjectName("exportButton")
        self.exportButton.clicked.connect(self.on_export_clicked)
        self.progress = QtWidgets.QLabel(Dialog)
        self.progress.setGeometry(QtCore.QRect(20, 220, 151, 20))
        self.progress.setObjectName("progress")
        self.beginTimeView = QtWidgets.QDateTimeEdit(Dialog)
        self.beginTimeView.setGeometry(QtCore.QRect(10, 100, 194, 22))
        self.beginTimeView.setObjectName("beginTimeView")
        self.endTimeView = QtWidgets.QDateTimeEdit(Dialog)
        self.endTimeView.setGeometry(QtCore.QRect(10, 160, 194, 22))
        self.endTimeView.setObjectName("endTimeView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 80, 84, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 84, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "微信店铺"))
        self.label_status.setText(_translate("Dialog", "当前状态：未登录"))
        self.pushrefresh.setText(_translate("Dialog", "载入状态"))
        self.exportButton.setText(_translate("Dialog", "导出xlsx"))
        self.progress.setText(_translate("Dialog", "当前导出进度：0%"))
        self.label.setText(_translate("Dialog", "开始时间"))
        self.label_2.setText(_translate("Dialog", "结束时间"))
        # 7 days ago
        self.beginTimeView.setDateTime(QDateTime.currentDateTime().addDays(-7))
        self.endTimeView.setDateTime(QDateTime.currentDateTime())
        self.pushrefresh.hide()
        self.on_pushrefresh_clicked()

    def filterTime(self, currentDateTime):
        print(currentDateTime)
        currentPyDateTime = QDateTime.fromString(str(currentDateTime), "yyyy-MM-dd HH:mm:ss")
        beginTime = self.beginTimeView.dateTime().toPyDateTime()
        endTime = self.endTimeView.dateTime().toPyDateTime()
        if currentPyDateTime < beginTime:
            return 1
        elif currentPyDateTime > endTime:
            return 2
        else:
            return 0

    def exportData(self):
        init_xml(self.path)

        result = get_order_list(1, None, self.custom_cookie)
        totalPage = 0
        nextKey = ""
        bizuin = ""
        for order in result:
            if order.bizuin != "":
                bizuin = order.bizuin
            totalPage = order.totalPage
            nextKey = order.nextKey
            if order.total_address.find("*") != -1:
                order.total_address = order_detail(order.orderId, bizuin, self.custom_cookie)
            if self.filterTime(order.createTime) == 0:
                append_xml(order.orderId, order.createTime, order.status, order.goodsName, order.productCnt,
                           order.total_address)
        print(totalPage)
        progress = 100 / totalPage - 5
        progress_string = f"{progress:.1f}"
        self.progress.setText(f"当前导出进度：{progress_string}%")
        self.breakFlag = False
        for i in range(2, totalPage + 1):
            result = get_order_list(i, nextKey, self.custom_cookie)
            self.breakFlag = False
            for order in result:
                if order.bizuin != "":
                    bizuin = order.bizuin
                nextKey = order.nextKey
                if order.total_address.find("*") != -1:
                    order.total_address = order_detail(order.orderId, bizuin, self.custom_cookie)
                timeflag = self.filterTime(order.createTime)
                print("timeflag", timeflag)
                if timeflag == 0:
                    append_xml(order.orderId, order.createTime, order.status, order.goodsName, order.productCnt,
                               order.total_address)
                elif timeflag == 1:
                    self.breakFlag = True

            if self.breakFlag:
                break

            progress = 100 * i / totalPage - 5
            progress_string = f"{progress:.1f}"
            self.progress.setText(f"当前导出进度：{progress_string}%")

        save_xml(self.path)
        progress = 100
        progress_string = f"{progress:.1f}"
        self.progress.setText(f"当前导出进度：已完成")

    def readCookies(self):

        self.custom_cookie = "45"
        if os.path.exists('cookies.ini'):
            with open('cookies.ini', 'r') as f:
                self.custom_cookie = cookie_dict_to_str(f.read())
        print(self.custom_cookie)

        # print type
        if not test_login(self.custom_cookie):
            url = "https://channels.weixin.qq.com/shop-faas/mmecnodelogin/getLoginQrCode?token=&lang=zh_CN&login_appid="

            headers = {
                "Host": "channels.weixin.qq.com",
                "Connection": "keep-alive",
                "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                "Accept": "application/json, text/plain, */*",
                "sec-ch-ua-mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "sec-ch-ua-platform": '"Windows"',
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://channels.weixin.qq.com/shop",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ja-JP;q=0.6,ja;q=0.5",
            }

            response = requests.get(url, headers=headers,verify=False)
            json_data = json.loads(response.text)
            qrcodeImg = json_data["qrcodeImg"]
            qrTicket = json_data["qrTicket"]

            print(qrcodeImg)
            print(qrTicket)
            base64_string = qrcodeImg
            decoded_bytes = base64.b64decode(base64_string)
            with open('qrcode.png', 'wb') as f:
                f.write(decoded_bytes)
            pixmap = QtGui.QPixmap( 'qrcode.png')

            # Scale the image to fit the label
            pixmap = pixmap.scaled(self.label_qr.size(), QtCore.Qt.KeepAspectRatio)

            self.label_qr.setPixmap(pixmap)
            while True:
                if query_login(qrTicket) == 3:
                    break
                time.sleep(2)
            with open('cookies.ini', 'r') as f:
                self.custom_cookie = cookie_dict_to_str(f.read())

        self.label_qr.hide()
        if os.path.exists("qrcode.png"):
            os.remove("qrcode.png")
        self.label_status.setText("当前状态：已登录")
        return self.custom_cookie
