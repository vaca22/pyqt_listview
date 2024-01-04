# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from login import Ui_Login_Form


class Ui_MainWindow(object):
    def __init__(self):
        self.username = None
        self.password = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(19, 9, 711, 481))
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.ui_login=Ui_Login_Form()
        self.ui_login.setupUi(self.login_page)
        self.ui_login.pushButton.clicked.connect(self.loginClick)


        self.login_page.setObjectName("page")
        self.stackedWidget.addWidget(self.login_page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
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


        # Layout for the first page
        # first_page_layout = QtWidgets.QVBoxLayout(self.login_page)



    def loginClick(self):
        # Switch to the second page
        self.username = self.ui_login.username_et.text()
        self.password = self.ui_login.password_et.text()
        if(self.username == 'admin' and self.password == 'admin'):
            self.stackedWidget.setCurrentIndex(1)
        else:
            QMessageBox.warning(self.login_page, "提示", "用户名或密码错误")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "微信店铺订单导出工具"))

