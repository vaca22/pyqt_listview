# -*- coding: utf-8 -*-
import base64
import json
import os
import time
from threading import Thread

import requests
# Form implementation generated from reading ui file 'TestDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from order_detail import order_detail
from order_list import get_order_list
from query_login import query_login
from test_login import test_login
from xml_save import init_xml, append_xml, save_xml


class Ui_Dialog(object):

    def __init__(self):
        self.thread = None
        self.custom_cookie = ""

    def on_pushrefresh_clicked(self):
        print("pushrefresh button was clicked")
        #check if thread is None
        if self.thread is None:
            self.thread = Thread(target=self.readCookies)
            self.thread.start()
            return

        print("thread is alive")


    def on_export_clicked(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(None, "导出xlsx位置", "",
                                                            "Text Files (*.xlsx)", options=options)
        if fileName:
            fileName = fileName + ".xlsx"
            print(fileName)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(454, 399)
        self.label_qr = QtWidgets.QLabel(Dialog)
        self.label_qr.setGeometry(QtCore.QRect(140, 50, 241, 261))
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
        self.exportButton.setGeometry(QtCore.QRect(330, 350, 75, 24))
        self.exportButton.setObjectName("exportButton")
        self.exportButton.clicked.connect(self.on_export_clicked)
        self.progress = QtWidgets.QLabel(Dialog)
        self.progress.setGeometry(QtCore.QRect(20, 350, 151, 20))
        self.progress.setObjectName("progress")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "微信店铺"))
        self.label_status.setText(_translate("Dialog", "当前状态：未登录"))
        self.pushrefresh.setText(_translate("Dialog", "刷新二维码"))
        self.exportButton.setText(_translate("Dialog", "导出xlsx"))
        self.progress.setText(_translate("Dialog", "当前导出进度：0%"))

    def exportData(self):
        init_xml()
        result_total = []
        result = get_order_list(1, None, self.custom_cookie)
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
            result = get_order_list(i, nextKey, self.custom_cookie)
            result_total.extend(result)
            for order in result:
                if order.bizuin != "":
                    bizuin = order.bizuin
                nextKey = order.nextKey

        for order in result_total:
            if order.total_address.find("*") != -1:
                order.total_address = order_detail(order.orderId, bizuin, self.custom_cookie)
            append_xml(order.orderId, order.createTime, order.status, order.goodsName, order.productCnt,
                       order.total_address)
        save_xml()
        
    def readCookies(self):
        self.custom_cookie = ""
        if os.path.exists('cookies.txt'):
            with open('cookies.txt', 'r') as f:
                self.custom_cookie = f.read()
        print(self.custom_cookie)
        # print type
        if not test_login(self.custom_cookie):
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
            pixmap = QtGui.QPixmap("qrcode.png")

            # Scale the image to fit the label
            pixmap = pixmap.scaled(self.label_qr.size(), QtCore.Qt.KeepAspectRatio)

            self.label_qr.setPixmap(pixmap)
            while True:
                if query_login(qrTicket) == 3:
                    break
                time.sleep(2)
            with open('cookies.txt', 'r') as f:
                self.custom_cookie = f.read()
        self.label_status.setText("当前状态：已登录")
        return self.custom_cookie
