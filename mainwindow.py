# -*- coding: utf-8 -*-
import base64
import json
import os
import time
from threading import Thread

import requests
# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QMessageBox

from QRCodeWindow import QRCodeWindow
from admin import register, login_admin, use_point
from cookies_convert import cookie_dict_to_str
from export_form import Ui_ExportForm
from login import Ui_Login_Form
from order_detail import order_detail
from order_list import get_order_list
from query_login import query_login
from register import Ui_Register_Form
from test_login import test_login
from xml_save import save_xml, append_xml, init_xml


class Ui_MainWindow(object):
    def __init__(self):
        self.userData = None
        self.username = None
        self.password = None
        self.breakFlag = None
        self.refreshThread = None
        self.path = None
        self.exportThread = None
        self.settings = QtCore.QSettings("settings.ini", "wx_shop_settings")
        self.custom_cookie = self.settings.value("cookie", "")

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(19, 9, 711, 481))
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.ui_login = Ui_Login_Form()
        self.ui_login.setupUi(self.login_page)
        self.ui_login.password_et.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui_login.pushButton.clicked.connect(self.loginClick)
        self.ui_login.register_bt.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        self.login_page.setObjectName("login_page")
        self.stackedWidget.addWidget(self.login_page)

        self.register_page = QtWidgets.QWidget()
        self.ui_register = Ui_Register_Form()
        self.ui_register.setupUi(self.register_page)
        self.ui_register.register_bt.clicked.connect(self.registerClick)
        self.ui_register.password_et.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui_register.password2_et.setEchoMode(QtWidgets.QLineEdit.Password)

        self.stackedWidget.addWidget(self.register_page)

        self.export_page = QtWidgets.QWidget()
        self.export_page.setObjectName("export_form")

        self.ui_export = Ui_ExportForm()
        self.ui_export.setupUi(self.export_page)

        self.ui_export.status_drop.addItems(["全部", "已完成", "待发货"])
        self.ui_export.export_bt.clicked.connect(self.exportClick)
        self.ui_export.recharge.clicked.connect(self.rechargeClick)
        self.ui_export.switch_account.clicked.connect(self.resetCookie)
        self.ui_export.logout.clicked.connect(self.logoutClick)

        self.stackedWidget.addWidget(self.export_page)

        if self.loginAuto():
            self.stackedWidget.setCurrentIndex(2)
        else:
            self.stackedWidget.setCurrentIndex(0)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def registerClick(self):
        print("register")
        username = self.ui_register.username_et.text()
        password = self.ui_register.password_et.text()
        password2 = self.ui_register.password2_et.text()
        tel = self.ui_register.tel_et.text()
        if username == "" or password == "" or password2 == "" or tel == "":
            QMessageBox.warning(self.register_page, "提示", "请填写完整信息")
            return
        if password != password2:
            QMessageBox.warning(self.register_page, "提示", "两次密码不一致")
            return
        tel = self.ui_register.tel_et.text()
        if len(tel) != 11:
            QMessageBox.warning(self.register_page, "提示", "手机号码格式错误")
            return
        if register(username, password, tel):
            QMessageBox.information(self.register_page, "提示", "注册成功")
            self.stackedWidget.setCurrentIndex(0)

    def rechargeClick(self):
        print("recharge")
        qr_widget = QRCodeWindow("Your text here",self.MainWindow)
        qr_widget.show()

    def exportClick(self):
        if self.userData.point <= 0:
            QMessageBox.warning(self.export_page, "提示", "点数不足")
            return


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

    def loginAuto(self):
        self.username = self.settings.value("username", "")
        self.password = self.settings.value("password", "")
        self.userData = login_admin(self.username, self.password)
        if self.userData is not None:
            print("login success")
            self.settings.setValue("username", self.username)
            self.settings.setValue("password", self.password)
            self.ui_export.remain_point.setText(f"剩余点数：{self.userData.point}")
            self.stackedWidget.setCurrentIndex(2)
            self.ui_export.end_date.setDateTime(QtCore.QDateTime.currentDateTime())
            self.ui_export.begin_date.setDateTime(QtCore.QDateTime.currentDateTime().addDays(-7))

            if self.refreshThread is None:
                self.refreshThread = Thread(target=self.readCookies)
                self.refreshThread.start()
            return True
        else:
            return False

    def loginClick(self):
        # Switch to the second page
        self.username = self.ui_login.username_et.text()
        self.password = self.ui_login.password_et.text()
        self.userData = login_admin(self.username, self.password)
        if self.userData is not None:
            print("login success")
            self.settings.setValue("username", self.username)
            self.settings.setValue("password", self.password)
            self.ui_export.remain_point.setText(f"剩余点数：{self.userData.point}")
            self.stackedWidget.setCurrentIndex(2)
            self.ui_export.end_date.setDateTime(QtCore.QDateTime.currentDateTime())
            self.ui_export.begin_date.setDateTime(QtCore.QDateTime.currentDateTime().addDays(-7))

            if self.refreshThread is None:
                self.refreshThread = Thread(target=self.readCookies)
                self.refreshThread.start()
        else:
            QMessageBox.warning(self.login_page, "提示", "用户名或密码错误")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "微信店铺订单导出工具"))

    def logoutClick(self):
        self.settings.setValue("username", "")
        self.settings.setValue("password", "")
        self.stackedWidget.setCurrentIndex(0)

    def resetCookie(self):
        self.custom_cookie = ""
        self.settings.setValue("cookie", self.custom_cookie)
        if self.refreshThread is None:
            self.refreshThread = Thread(target=self.readCookies)
            self.refreshThread.start()

    def filterTime(self, currentDateTime, status):
        print(currentDateTime)
        currentPyDateTime = QDateTime.fromString(str(currentDateTime), "yyyy-MM-dd HH:mm:ss")
        beginDate = self.ui_export.begin_date.date()
        beginDateTime = self.ui_export.begin_time.time()
        beginTime = QDateTime(beginDate, beginDateTime)
        endDate = self.ui_export.end_date.date()
        endDateTime = self.ui_export.end_time.time()
        endTime = QDateTime(endDate, endDateTime)
        wantStatus = self.ui_export.status_drop.currentIndex()
        if currentPyDateTime < beginTime:
            return 1
        elif currentPyDateTime > endTime:
            return 2
        else:
            if wantStatus == 0:
                return 0
            elif wantStatus == 1:
                if status == "已完成":
                    return 0
                elif status == "已发货":
                    return 0
                else:
                    return 3
            elif wantStatus == 2:
                if status == "待发货":
                    return 0
                else:
                    return 3

    def exportData(self):
        init_xml(self.path)
        export_num = 0

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
            if self.filterTime(order.createTime, order.status) == 0:
                append_xml(order.orderId, order.createTime, order.status, order.goodsName, order.productCnt,
                           order.total_address)
                export_num += 1
        print(totalPage)
        progress = 100 / totalPage - 5
        progress_string = f"{progress:.1f}"
        self.ui_export.export_status.setText(f"进度：{progress_string}%")
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
                timeflag = self.filterTime(order.createTime, order.status)
                print("timeflag", timeflag)
                if timeflag == 0:
                    append_xml(order.orderId, order.createTime, order.status, order.goodsName, order.productCnt,
                               order.total_address)
                    export_num += 1
                elif timeflag == 1:
                    self.breakFlag = True

            if self.breakFlag:
                break

            progress = 100 * i / totalPage - 5
            progress_string = f"{progress:.1f}"
            self.ui_export.export_status.setText(f"进度：{progress_string}%")

        save_xml(self.path)
        self.userData.point -= export_num
        if self.userData.point < 0:
            export_num = self.userData.point
            self.userData.point = 0

        self.ui_export.remain_point.setText(f"剩余点数：{self.userData.point}")
        use_point(self.userData.userId, self.userData.token, export_num)
        progress = 100
        progress_string = f"{progress:.1f}"
        self.ui_export.export_status.setText(f"进度：已完成")

    def readCookies(self):
        # print type
        if not test_login(self.custom_cookie):
            self.ui_export.login_status.setText("状态：未登录")

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

            response = requests.get(url, headers=headers, verify=False)
            json_data = json.loads(response.text)
            qrcodeImg = json_data["qrcodeImg"]
            qrTicket = json_data["qrTicket"]

            print(qrcodeImg)
            print(qrTicket)
            base64_string = qrcodeImg
            decoded_bytes = base64.b64decode(base64_string)

            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(decoded_bytes)

            # Scale the image to fit the label
            pixmap = pixmap.scaled(self.ui_export.qrcode.size(), QtCore.Qt.KeepAspectRatio)

            self.ui_export.qrcode.setPixmap(pixmap)
            self.ui_export.qrcode.show()
            while True:
                self.custom_cookie = query_login(qrTicket)
                if self.custom_cookie is not None:
                    break
                time.sleep(2)
            self.settings.setValue("cookie", self.custom_cookie)

        self.ui_export.qrcode.hide()
        self.ui_export.export_status.setText("进度：未开始")
        self.ui_export.export_status.show()
        self.ui_export.export_status.adjustSize()
        self.ui_export.login_status.setText("状态：已登录")
        self.refreshThread = None
        return self.custom_cookie
